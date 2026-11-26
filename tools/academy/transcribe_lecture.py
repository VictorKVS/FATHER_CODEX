#!/usr/bin/env python3
"""Transcribe an OWNED/authorized educational video. Output is ASR DRAFT, not verbatim verified.
Python 3.10+. Requires: pip install faster-whisper
ffmpeg CLI must be installed and on PATH.
Example: python transcribe_lecture.py "M0_Ls1.mp4" --model large-v3 --device cpu
"""
import argparse
import json
import shutil
import subprocess
import tempfile
import wave
from pathlib import Path


def stamp(seconds: float, separator: str) -> str:
    ms = max(0, round(seconds * 1000))
    h, rem = divmod(ms, 3600000)
    m, rem = divmod(rem, 60000)
    s, milli = divmod(rem, 1000)
    return f"{h:02d}:{m:02d}:{s:02d}{separator}{milli:03d}"


def main():
    p = argparse.ArgumentParser(description="Draft Russian lecture transcript with timestamps.")
    p.add_argument("video", type=Path)
    p.add_argument("--model", default="medium", help="medium or large-v3 (downloaded first use)")
    p.add_argument("--device", default="cpu", choices=["cpu", "cuda", "auto"])
    p.add_argument("--compute-type", default=None, help="e.g. int8 for CPU, float16 for supported CUDA")
    p.add_argument("--output-dir", type=Path, default=None)
    args = p.parse_args()
    src = args.video.expanduser().resolve()
    if not src.is_file():
        p.error(f"File not found: {src}")
    if not shutil.which("ffmpeg"):
        p.error("ffmpeg not found on PATH. Install FFmpeg first.")
    try:
        from faster_whisper import WhisperModel
    except ImportError as err:
        p.error(f"Missing faster-whisper: python -m pip install faster-whisper ({err})")
    outdir = (args.output_dir or src.parent).resolve()
    outdir.mkdir(parents=True, exist_ok=True)
    base = outdir / f"{src.stem}.asr-draft"
    with tempfile.TemporaryDirectory() as work:
        wav = Path(work) / "audio.wav"
        subprocess.run(["ffmpeg", "-nostdin", "-hide_banner", "-loglevel", "error", "-y",
                        "-i", str(src), "-vn", "-ac", "1", "-ar", "16000", "-c:a", "pcm_s16le",
                        str(wav)], check=True)
        with wave.open(str(wav)) as track:
            duration = track.getnframes() / track.getframerate()
        print(f"Audio duration: {duration:.1f}s. Model: {args.model}. Device: {args.device}.")
        model = WhisperModel(args.model, device=args.device,
                             compute_type=args.compute_type or ("int8" if args.device == "cpu" else "auto"))
        segments, info = model.transcribe(str(wav), language="ru", beam_size=5,
                                          vad_filter=True, condition_on_previous_text=True)
        entries = [{"start": float(seg.start), "end": float(seg.end), "text": seg.text.strip(),
                    "avg_logprob": float(seg.avg_logprob), "no_speech_prob": float(seg.no_speech_prob)}
                   for seg in segments if seg.text.strip()]
    metadata = {"source": src.name, "status": "ASR_DRAFT_REQUIRES_LISTENING_VERIFICATION",
                "model": args.model, "device": args.device, "detected_language": info.language,
                "audio_duration_seconds": duration, "segments": entries}
    (Path(str(base) + ".json")).write_text(json.dumps(metadata, ensure_ascii=False, indent=2), encoding="utf-8")
    with (Path(str(base) + ".srt")).open("w", encoding="utf-8") as output:
        for n, e in enumerate(entries, start=1):
            output.write(f"{n}\n{stamp(e['start'], ',')} --> {stamp(e['end'], ',')}\n{e['text']}\n\n")
    with (Path(str(base) + ".txt")).open("w", encoding="utf-8") as output:
        output.write("АВТОМАТИЧЕСКАЯ ЧЕРНОВАЯ ТРАНСКРИПЦИЯ. НЕ СЧИТАТЬ ДОСЛОВНОЙ БЕЗ СВЕРКИ.\n\n")
        for e in entries:
            output.write(f"[{stamp(e['start'], '.')}–{stamp(e['end'], '.')}] {e['text']}\n")
    print(f"ASR draft generated: {base}.txt, {base}.srt, {base}.json")
    print("Mandatory next step: listen and correct terminology, names, negations, timestamps.")


if __name__ == "__main__":
    main()
