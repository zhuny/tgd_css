
var CSS_DOM_ID = "zhuny_custom_css";
var TEXT_DOM_ID = "zhuny_textarea";

function create_textarea() {
  var t = document.createElement("textarea");
  t.style.width = "100%";
  t.style.resize = "none";
  t.style.height = "200px";
  t.id = TEXT_DOM_ID;
  return t;
}

function create_button() {
  var b = document.createElement("button");
  b.addEventListener("click", put_style);
  b.innerText = "적용하기";
  b.style.width = "100%";
  b.style.height = "50px";
  return b;
}

function create_style() {
  var s = document.createElement("style");
  var h = document.head;
  s.id = CSS_DOM_ID;
  s.type = "text/css";
  h.appendChild(s);
}

function create_div() {
  var d = document.createElement("div");
  d.style.position = "fixed";
  d.style.bottom = 0;
  d.style.left = 0;
  d.style.right = 0;
  d.append(create_textarea());
  d.append(create_button());
  document.body.append(d);
}

function put_style() {
  var s = document.getElementById(CSS_DOM_ID);
  var t = document.getElementById(TEXT_DOM_ID);
  s.remove();
  s.innerText = "";
  s.appendChild(document.createTextNode(t.value));
  document.head.appendChild(s);
}

create_div();
create_style();

