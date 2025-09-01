// Comentarios falsos
const comentarios = [
  "Esto funciona de verdad 🔥",
  "Muy bueno, ya me impactó el saldo 👌",
  "Increíble, gracias 🙏",
  "Mejor que cualquier otra cosa",
  "Ya bajé 2 apps, todo perfecto!"
];
const ul = document.getElementById("comentarios");
comentarios.forEach(c => {
  const li = document.createElement("li");
  li.textContent = c;
  ul.appendChild(li);
});
