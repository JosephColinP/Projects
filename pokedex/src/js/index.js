import "bootstrap/dist/css/bootstrap.min.css";
import * as bootstrap from "bootstrap";
import axios from "axios";
import "../styles/main.css";

const pokemonAPI = process.env.POKEMON_API;
let pokemons = {};
let pokemon = {};
let pokemonData = {};
let changeBtn = document.getElementById("changeBtn");

const fetchPokemons = function () {
  return axios
    .get(pokemonAPI)
    .then(function (response) {
      pokemons = response.data.results;
      console.log(response.data.results);
      return pokemons;
    })
    .catch(function (err) {
      console.log(err);
    });
};

const fetchPokemon = async function () {
  try {
    await fetchPokemons();
    pokemon = pokemons[Math.floor(Math.random() * pokemons.length)];
    console.log(pokemon);
    return pokemon;
  } catch (err) {
    console.log(err);
  }
};

const fetchPokeData = async function () {
  try {
    await fetchPokemon();
    return axios.get(`${pokemon.url}`).then(function (response) {
      pokemonData = response.data;
      console.log(pokemonData);
    });
  } catch (err) {
    console.log(err);
  }
};

const writeData = function () {
  pokedexData.innerHTML = `
  <div id="pokeContainer" class="d-flex
    flex-column 
    justify-content-center">
    <div class="d-flex 
      justify-content-center 
      h-100 
      pokeBox"  
      style="background-color: #37796C"
      >
      <img src="${pokemonData.sprites.front_default}"
        class="w-75"
      >
    </div>
    <div class="d-flex 
      flex-column 
      justify-content-center 
      align-items-center
      pokeBox"
      
      style="background-color: #CE2211"
      >
        <h2>${pokemonData.name}</h2>
        <p><b>Abilities:</b> ${pokemonData.abilities[0].ability.name}</p>
        <p><b>Height:</b> ${pokemonData.height}</p>
        <p><b>Weight:</b> ${pokemonData.weight}</p>
    </div>
  </div>
  `;
};

const showData = async function () {
  try {
    await fetchPokeData();
    writeData();
  } catch (err) {
    console.log(err);
  }
};

const repeatShowData = function () {
  showData();
  setInterval(showData, 10000);
};

repeatShowData();

changeBtn.onclick = function () {
  showData();
};
