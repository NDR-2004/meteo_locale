document.getElementById("rechercher").addEventListener("click", () => {
  const ville = document.getElementById("ville").value;

  fetch(`/api/meteo?ville=${ville}`)
    .then(res => res.json())
    .then(data => {
      if (data.error) {
        document.getElementById("resultats").textContent = data.error;
        return;
      }

      document.getElementById("temperature").textContent = `Température : ${data.temperature} °C`;
      document.getElementById("description").textContent = `Description : ${data.description}`;
      document.getElementById("vent").textContent = `Vent : ${data.vent} m/s`;
    })
    .catch(err => {
      console.error(err);
      document.getElementById("resultats").textContent = "Erreur serveur";
    });
});
