const poke_container = document.querySelector(".poke-container");

const pokedexBG_Colors = {
	fire: '#fddfgf', grass: '#defde0',	electric: '#fcf7de', water: '#def3fd', ground: '#f4e7da', rock: '#D5D5D4',	fairy: '#FCEAFF',
	poison: '#98D7A5', bug: '#F8d5A3', dragon: '#97D3E6', psychic: '#EAEDA1', flying: '#f5f5f5', fighting: '#e6e0d4', normal: '#F5F5F5'
};

const all_types = Object.keys(pokedexBG_Colors);

const pokemonsCount = async () => {
	for (let i = 1; i <= 54; i++) {
		await getPokedex(i);
	}
};

const getPokedex = async id => {

	const url = `https://pokeapi.co/api/v2/pokemon/${id}`;

	const res = await fetch(url);

	const pokemon = await res.json();

	makePokedexCard(pokemon);
};


function makePokedexCard(pokemon) {

	const pokedexEl = document.createElement('div');

	pokedexEl.classList.add('pokedex');

	const poke_types = pokemon.types.map(type => type.type.name);

	const type = all_types.find( type => poke_types.indexOf(type) > -1);

	const name = pokemon.name[0].toUpperCase() + pokemon.name.slice(1);

	const color = pokedexBG_Colors[type];
	
	pokedexEl.style.backgroundColor = color;

	const pokeInnerHTML = `
        <div class="img-div">
            <img src="https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/versions/generation-vi/x-y/${pokemon.id}.png" alt="${name}" />
        </div>

        <div class="infos">
            <span class="number">#${pokemon.id.toString().padStart(3, '0')}</span>
            <h3 class="name">${name}</h3>
            <small class="type">Type: <span>${type}</span></small>
        </div>
    `;

	pokedexEl.innerHTML = pokeInnerHTML;

	poke_container.appendChild(pokedexEl);
}

pokemonsCount();

