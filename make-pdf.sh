makepdf()
{
  FILEWEB="pdf/${1}-conferences.pdf"
  FILEPRINT="pdf/${1}-conferences-print.pdf"
  #ADDR="http://localhost:8080/${1}"
  ADDR="${1}.html"
  TIME=10000
  echo "Je vais créer ${FILEPRINT}, ça va prendre environ $(($TIME/1000)) secondes."
  chromium --headless --disable-gpu --print-to-pdf=$FILEPRINT $ADDR --run-all-compositor-stages-before-draw --timeout=$TIME;
  echo "Maintenant je vais créer ${FILEWEB}."
  ps2pdf -dPDFSETTINGS=/ebook $FILEPRINT $FILEWEB
}

makepdf dossier;  
#makepdf livre;  
