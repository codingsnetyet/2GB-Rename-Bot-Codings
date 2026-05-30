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

            vcodec="copy",
            acodec="copy",

            map=["0:v:0", "0:a?", "0:s?"],  

            map_metadata="-1",

            movflags="+faststart",

            # ONLY GLOBAL METADATA (SAFE)
            **{
                "metadata": f"title={title}",
                "metadata:g": f"artist={artist}",
                "metadata:g:1": f"author={author}",
            }
        )

        ffmpeg.run(stream, overwrite_output=True)

        if not os.path.exists(output_file):
            return input_file

        if os.path.getsize(output_file) < 100000:
            return input_file

        return output_file

    except Exception as e:
        print("⚠️ COPY FAILED:", e)

        try:
            stream = ffmpeg.input(input_file)

            stream = ffmpeg.output(
                stream,
                output_file,

                vcodec="copy",
                acodec="copy",

                movflags="+faststart",

                **{
                    "metadata": f"title={title}",
                    "metadata:g": f"artist={artist}",
                    "metadata:g:1": f"author={author}",
                }
            )

            ffmpeg.run(stream, overwrite_output=True)
            return output_file

        except Exception as e2:
            print("❌ FALLBACK FAILED:", e2)
            return input_file


# ------------------------- #
# Don't Remove Credit 
# Ask Doubt @AU_Bot_Discussion 
# Owner @Mr_Mohammed_29 
# ------------------------- #
