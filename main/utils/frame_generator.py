
def frame_generator(frame_duration_ms,
                    audio,
                    sample_rate):
    """Generates audio frames from PCM audio data.
    Takes the desired frame duration in milliseconds, the PCM data, and
    the sample rate.
    Yields Frames of the requested duration.
    """
    n = int(sample_rate * (frame_duration_ms / 1000.0) *2 )
    offset = 0
    
    while offset + n < len(audio):
        yield audio[offset:offset + n]
        offset += n   