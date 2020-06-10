# Download MVTec Anomaly Detection Dataset (MVTec AD)
mkdir -p data/mvtec
wget ftp://guest:GU.205dldo@ftp.softronics.ch/mvtec_anomaly_detection/mvtec_anomaly_detection.tar.xz
mv mvtec_anomaly_detection.tar.xz data/mvtec
cd data/mvtec
tar -xf mvtec_anomaly_detection.tar.xz
rm mvtec_anomaly_detection.tar.xz
