function randomColor () {
    const r = Math.floor(Math.random()*256)
    const g = Math.floor(Math.random()*256)
    const b = Math.floor(Math.random()*256)
    return`rgb(${r},${g},${b})`
  }
  let divColoré = document.querySelector("#div-colore")
  divColoré.onclick = () => {
    divColoré.style.background = randomColor()
  }
  