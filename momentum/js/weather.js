const API_KEY = "b45698e5d6e6ba1c3399ae199d545d25"

navigator.geolocation.getCurrentPosition(onGeoOk, onGeoErr);

function onGeoOk(position) {
  const lat = position.coords.latitude;
  const lon = position.coords.longitude;
  const url = `https://api.openweathermap.org/data/2.5/weather?lat=${lat}&lon=${lon}&appid=${API_KEY}&units=metric`;
  fetch(url)
    .then((response) => response.json()) //response의 json을 얻고 그 결과로 다음 작업 진행
    .then((data) => {
      const weatherIcon = document.createElement("img");
      weatherIcon.src=`http://openweathermap.org/img/wn/${data.weather[0].icon}.png`;
      weatherIcon.alt="icon";
      const weatherRow = document.querySelector("#weather li:first-child");
      weatherRow.appendChild(weatherIcon);
      const temp = document.querySelector("#weather li:first-child span");
      const city = document.querySelector("#weather li:last-child span");
      temp.innerText = `${Math.ceil(data.main.temp)}°C`;
      city.innerText = data.name;
    });
}
function onGeoErr() {
  alert("Cant' find you. No weather infomation for you.")
}



const weatherContainer = document.querySelector("#weather");
weatherContainer.addEventListener("click",goToKMA);

function goToKMA() {
  window.open(
    "https://www.weather.go.kr/","_blank"
  );
}