NAME="streamlit"
docker build -t $NAME-img .
docker run -p 8501:8501 $NAME
