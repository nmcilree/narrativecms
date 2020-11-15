
// Initialise the container with the boxes in by giving a height so percentage top works
var chapter = document.getElementById("chapter");
chapter.style.height = (window.innerHeight - 40) + "px";

// Make the DIV element draggable:
var draggable_boxes = document.getElementsByClassName("box");
for (i = 0; i < draggable_boxes.length; i++) {
  dragElement(document.getElementById(draggable_boxes[i].id));
}

function dragElement(elmnt) {
  var pos1 = 0, pos2 = 0, pos3 = 0, pos4 = 0;
  if (document.getElementById(elmnt.id + "header")) {
    // if present, the header is where you move the DIV from:
    document.getElementById(elmnt.id + "header").onmousedown = dragMouseDown;
  } else {
    // otherwise, move the DIV from anywhere inside the DIV:
    elmnt.onmousedown = dragMouseDown;
  }

  function dragMouseDown(e) {
    e = e || window.event;
    e.preventDefault();
    // get the mouse cursor position at startup:
    pos3 = e.clientX;
    pos4 = e.clientY;
    document.onmouseup = closeDragElement;
    // call a function whenever the cursor moves:
    document.onmousemove = elementDrag;
  }

  function elementDrag(e) {
    e = e || window.event;
    e.preventDefault();
    // calculate the new cursor position:
    pos1 = pos3 - e.clientX;
    pos2 = pos4 - e.clientY;
    pos3 = e.clientX;
    pos4 = e.clientY;

    // set the element's new position:
    elmnt.style.top = (elmnt.offsetTop - pos2) + "px";
    elmnt.style.left = (elmnt.offsetLeft - pos1) + "px";

    // re-establish the jsplumb line
    jsPlumb.revalidate(elmnt.id);
  }

  function closeDragElement() {
    // stop moving when mouse button is released:
    document.onmouseup = null;
    document.onmousemove = null;

    // Get the box position
    top_pos = (elmnt.offsetTop - pos2);
    left_pos = (elmnt.offsetLeft - pos1);

    // Get the box id
    id = elmnt.getAttribute('data-id');

    // Update page model of new location on page
    url = "/update_position?top=" + top_pos + "&left=" + left_pos + "&id=" + id;
    httpGet(url);

  }
}

function httpGet(url)
{
    var xmlHttp = new XMLHttpRequest();
    xmlHttp.open( "GET", url, false ); // false for synchronous request
    xmlHttp.send( null );
    return xmlHttp.responseText;
}
