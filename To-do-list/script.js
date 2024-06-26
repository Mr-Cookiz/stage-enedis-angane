let inputTodo = document.querySelector("#input-todo")

let mesTodos = [
  {
    label: "Faire des pizzas",
    fait: true
  },
  {
    label: "Faire les courses",
    fait: false
  },
  {
    label: "promener le chien",
    fait: false
  }
]

function rendu (mesTodos) {
  let todosContainer = document.querySelector("#todos-container")
  todosContainer.innerHTML = ""
  mesTodos.forEach((todo) => {
    let div = document.createElement("div")
    div.classList.add("todo")

    let monNouveauInput = document.createElement("input")
    monNouveauInput.type = "checkbox"
    monNouveauInput.checked = todo.fait
    monNouveauInput.onclick = () => {
      todo.fait = !todo.fait
    }

    let monNouveauParagraphe = document.createElement("p")
    monNouveauParagraphe.innerHTML = todo.label

    let monNouveauBouton = document.createElement("button")
    monNouveauBouton.classList.add("boutonSupprimer")
    monNouveauBouton.innerHTML = "supprimer"
    monNouveauBouton.onclick = () => {
      mesTodos.splice(mesTodos.indexOf(todo),1)
      console.log("bouton supprimer")
      rendu(mesTodos)
    }
    div.appendChild(monNouveauInput)
    div.appendChild(monNouveauParagraphe)
    div.appendChild(monNouveauBouton)
    let todosContainer = document.querySelector("#todos-container")
    todosContainer.appendChild(div)
  }
)}
rendu(mesTodos)

inputTodo.addEventListener("change", (e) => {
  console.log(e.target.value)
  mesTodos.push({
    label: e.target.value,
    fait: false
  })
  rendu(mesTodos)
})

let todosContainer = document.querySelector("#todos-container")
let Bouton = document.querySelector("#bouton")
Bouton.onclick = () => {
  mesTodos = []
  rendu(mesTodos)
  console.log("bouton")
}
let BoutonFait = document.querySelector("#boutonfait")
BoutonFait.classList.add("toutCocher")
BoutonFait.onclick = () => {
  mesTodos.forEach((todo) => {
    todo.fait = true
  })
  rendu(mesTodos)
  console.log("boutonfait")
}
