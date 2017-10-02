FAST stands for FAST is an Amplicon Sequencing Toolbox (as similar to GNU). It is a collection of Python script that can aid you in processing the high throughput sequencing data for marker gene (so it works for Bacteria too).

I have complied two example data set for a quick trial of FAST. The data set contains six soil samples sequenced on MiSeq 300 bp PE run either on ITS1 region or ITS2 region.

Here is the [pipeline](https://github.com/ZeweiSong/FAST/wiki/Fungal-ITS1-Pipeline-Using-Both-Reads) for processing the ITS1 data.

Here is a similar [pipeline](https://github.com/ZeweiSong/FAST/wiki/Fungal-ITS2-Pipeline-Using-Both-Reads) for processing the ITS2 data.

Both pipelines are now using pair-end merge instead of Read1 data. I have explain the reason for using pair-end merge in [this page](https://github.com/ZeweiSong/FAST/wiki/How-good-is-the-pair-end-merge%3F).

I have include a Linus shell script in the folder of both example data. If this is your first time trying FAST, I recommend visiting [this page](https://github.com/ZeweiSong/FAST/wiki/Setup-the-working-folder) for preparing the working environment of this pipeline.

If you still want to use only the Read1 data, here is an [example pipeline](https://github.com/ZeweiSong/FAST/wiki/Fungal-ITS1-Pipeline-Using-Read1-Sequences) using the same ITS1 data set. ITS2 data can be processed in a similar way.

I'm continuing update this wiki to provide more detailed information. Please let me know if you any suggestion or want to help. You can reach me with my email: `songzewei@outlook.com` or `songx208@umn.edu`.

Thanks for using FAST!
