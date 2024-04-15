sudo apt-get install gcc g++ cmake libjpeg8-dev

git clone https://github.com/jacksonliam/mjpg-streamer.git

# 소스파일에 이동
cd mjpg-streamer/mjpg-streamer-experimental

# 컴파일
make distclean
make CMAKE_BUILD_TYPE=Debug
sudo make install

export LD_LIBRARY_PATH=./mjpg-streamer/mjpg-streamer-experimental/
mjpg_streamer -o "output_http.so -w ./www -p 9090" -i "input_raspicam.so -fps 30 -preview"
