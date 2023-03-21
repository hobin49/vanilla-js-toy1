# 크롬 앱 Momentum 클론 프로젝트 
## 1. 제작 기간
* 2023/03/13 ~ 2022/03/21

</br>

## 2. 사용 기술
* HTML5
* CSS
* SASS
* JavaScript

</br>

## 3. 프로젝트 목표
* To Do 앱 클론 코딩을 통한 JavaScript 기초 학습
* 이전에 배웠던 HTML, CSS, SASS 복습
* 외부 API 활용

</br>

## 4. 주요 기능  
- 기본 구현  
  - [x] 랜덤 배경 이미지  
  - [x] 실시간 시계  
  - [x] 로컬 스토리지를 사용한 로그인  
  - [x] 로컬 스토리지를 사용한 투두리스트  
  - [x] 날씨와 위치 (geolocation)  
- 추가 구현   
  - [x] 반응형
  - [x] 사용자 리셋  
  - [x] 할 일 목록 취소선  
  - [x] 격언, 날씨 상세 링크  
  - [x] 날씨 상태에 맞는 아이콘 로딩  

</br>

## 5. 주요 코드
``` javascript

const toDoform = document.getElementById("toDo-form");
const toDoInput = toDoform.querySelector("input");
const TODOS_KEY = "toDos";
let toDos = [];

const savedToDos = localStorage.getItem(TODOS_KEY);

if (savedToDos !== null ) {
  const parsedToDos = JSON.parse(savedToDos);
  toDos = parsedToDos;
  parsedToDos.forEach(paintToDo);
}

toDoform.addEventListener("submit",handleToDoSubmit);

function handleToDoSubmit(event) {
  event.preventDefault();
  const newToDo = toDoInput.value;
  toDoInput.value="";
  const newToDoObj = {
    text:newToDo,
    id:Date.now()
  }
  toDos.push(newToDoObj);
  paintToDo(newToDoObj);
  saveToDos();
}

function paintToDo(newToDoObj) {
  const li = document.createElement("li");
  li.id = newToDoObj.id;
  
  const span = document.createElement("span");
  span.innerText = newToDoObj.text;
  span.addEventListener("click",checkingToDo);

  const button = document.createElement("button");
  button.innerText = "❌";
  button.addEventListener("click",deleteToDo);
  
  li.appendChild(span);
  li.appendChild(button);
  toDoList.appendChild(li); // greetings.js -- line 11
}

function saveToDos() {
  localStorage.setItem(TODOS_KEY, JSON.stringify(toDos));
}

function checkingToDo(event) {
  // const span = event.path[0]; //아래와 같음
  const span = event.target;
  span.classList.toggle("strikethrough");
}

function deleteToDo(event) {
  const li = event.target.parentElement;
  li.remove();
  toDos = toDos.filter((toDoObj) => toDoObj.id !== parseInt(li.id));
  //DOM에서는 삭제되었지만 변수로서의 li에서는 li.id 접근 가능
  //Element의 id는 문자열이기 때문에 숫자로 변환 필요
  saveToDos();
}
