# ------------------------- #
# Don't Remove Credit 
# Ask Doubt @AU_Bot_Discussion 
# Owner @Mr_Mohammed_29 
# ------------------------- #

import ffmpeg
import os

def add_metadata(input_file, output_file, title, author, artist, audio, subtitle, video):

    try:
        stream = ffmpeg.input(input_file)

        stream = ffmpeg.output(
            stream,
            output_file,
            codec="copy",
            map_metadata="-1",

            **{
                "metadata": f"title={title}",
                "metadata:g:artist": artist,
                "metadata:g:author": author,
                "metadata:s:a:0": f"title={audio}",
                "metadata:s:s:0": f"title={subtitle}",
                "metadata:s:v:0": f"title={video}",
            },

            movflags="faststart"
        )

        ffmpeg.run(stream, overwrite_output=True, quiet=True)

        return output_file

    except Exception as e:
        print("Metadata Error:", e)
        return input_file
# ------------------------- #
# Don't Remove Credit 
# Ask Doubt @AU_Bot_Discussion 
# Owner @Mr_Mohammed_29 
# ------------------------- #
