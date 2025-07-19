package main

import (
    "io/ioutil"
    "net/http"
)

func handler(w http.ResponseWriter, r *http.Request) {
    file := r.URL.Query().Get("file") // ?file=../../etc/passwd
    data, _ := ioutil.ReadFile(file)
    w.Write(data)
}

func main() {
    http.HandleFunc("/", handler)
    http.ListenAndServe(":8080", nil)
}
