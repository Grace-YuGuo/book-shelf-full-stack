// Get the anchor element inside the same span
const anchorElement = document.querySelector('.text-break.flex-grow-1 >a');
// Assign the anchor's href attribute to span innerHTML
anchorElement.innerHTML = anchorElement.href;