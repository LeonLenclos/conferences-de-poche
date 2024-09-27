makepdf()
{
  ADDR="http://0.0.0.0:8881/"
  HTML=$1
  FILEWEB=$2
  FILEPRINT="${2%.pdf}-print.pdf"
  TIME=10000
  python3 -m http.server 8881 &
  SERVER_PID=$!
  echo "Je vais créer ${FILEPRINT}, ça va prendre environ $(($TIME/1000)) secondes."
  chromium --headless --disable-gpu --no-pdf-header-footer --print-to-pdf=$FILEPRINT $ADDR$HTML --run-all-compositor-stages-before-draw --timeout=$TIME;
  echo "Maintenant je vais créer ${FILEWEB}."
  ps2pdf -dPDFSETTINGS=/ebook $FILEPRINT $FILEWEB
  kill $SERVER_PID;
}


makepdf $1 $2;
