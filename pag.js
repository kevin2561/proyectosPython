let img = [];
img[0] = "imagenes/img1.jpg";
img[1] = "imagenes/img2.jpg";
img[2] = "imagenes/img3.jpg";
img[3] = "imagenes/img4.jpg";
img[4] = "imagenes/img5.jpg";
img[5] = "imagenes/img6.jpg";
img[6] = "imagenes/img7.jpg";
img[7] = "imagenes/img8.jpg";
img[8] = "imagenes/img9.jpg";



let siguiente = document.querySelector("#btn-siguiente");
let atras = document.querySelector("#btn-atras");
let posicionImagen = document.querySelector("#posicion-img");
let verImg = document.querySelector("#visor");

let posicion = 0;
verImg.src = img[posicion];


posicionImagen.innerHTML = posicion + 1;




siguiente.addEventListener("click", function () {
    if (posicion < img.length - 1) {
        posicion++;
        actualizar();
    }


});
atras.addEventListener("click", function () {
    if (posicion > 0) {
        posicion--;
        actualizar();


    }
});

function actualizar() {
    verImg.src = img[posicion];
    posicionImagen.innerHTML = posicion + 1;
};

let x = 3;
/*

for (let i = 1; i < img.length; i++) {
    img[i] = `imagenes/img${i}.jpg`
}
for

*/
for (let i = 0; i < 3; i++) {
    console.log(i)

}
