const edit = (id, estado, cidade) => {
  document.getElementById("edit").style.display = "flex";
  document.getElementById("resultados").style.display = "none";
  document.getElementById("barraPesquisa").style.display = "none";

  document.getElementById("inputEstado").value = estado;
  document.getElementById("inputCidade").value = cidade;

  console.log(cidade, estado, id);
};

const menu = () => {
  document.getElementById("edit").style.display = "none";
  document.getElementById("resultados").style.display = "flex";
  document.getElementById("barraPesquisa").style.display = "flex";
};

const remover = (id) => {
  if (confirm("Tem certeza que deseja remover o item?")) {
    fetch(`/deletar/${id}`, {
      method: "POST",
    });
  }
  console.log(id);
};
