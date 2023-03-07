echo "Starting processing phase..."
location=$(cat tmp/location.txt)
set_number=$(cat tmp/number.txt)
cd $location/raw
echo "Converting raw photos to jpgs..."

for f in *; do
    if [[ $f == *.jpg ]]; then
        echo "Skipping $f"
    else
        echo "Converting $f to jpg"
        ffmpeg -y -i $f $f.jpg
    fi
done

echo "Converting jpgs to 1000x1000 jpgs..."
mkdir -p $location/processed/1000
for f in *.jpg; do
    echo "Converting $f to 1000x1000 jpg"
    ffmpeg -y -i $f -vf scale=1000:1000 $location/processed/1000/$f
done

echo "Creating black and white photos..."
mkdir -p $location/processed/bw
for f in *.jpg; do
    echo "Converting $f to black and white"
    ffmpeg -y -i $f -vf format=gray $location/processed/bw/$f
done

echo "Creating black and white 1000x1000 photos..."
mkdir -p $location/processed/bw_1000
for f in *.jpg; do
    echo "Converting $f to black and white 1000x1000"
    ffmpeg -y -i $f -vf format=gray,scale=1000:1000 $location/processed/bw_1000/$f
done

echo "Creating gif from 1000x1000 jpgs..."
ffmpeg -y -framerate 2 -i $location/processed/1000/%*.jpg $location/photos.gif

echo "Creating gif from 1000x1000 back and white jpgs..."
ffmpeg -y -framerate 2 -i $location/processed/bw_1000/%*.jpg $location/photos_bw.gif

echo "Creating blue channel photos..."
echo "Done processing photos"
echo "Purging temp"
rm -rf $location/raw
echo "Creating readme"
echo "# Open Sky set" $set_number > $location/README.md
echo "This set was automatically generated by Open Sky." >> $location/README.md
echo "[Click here for dataset info](https://github.com/awesomelewis2007/opensky/blob/master/dataset/$set_number/info.json)" >> $location/README.md
echo "## Photos preview" >> $location/README.md

echo "<img src=\"https://raw.githubusercontent.com/awesomelewis2007/opensky/master/dataset/$set_number/photos.gif\" width=\"200px\"/>" >> $location/README.md
echo "<img src=\"https://raw.githubusercontent.com/awesomelewis2007/opensky/master/dataset/$set_number/photos_bw.gif\" width=\"200px\"/>" >> $location/README.md

echo "Done"

