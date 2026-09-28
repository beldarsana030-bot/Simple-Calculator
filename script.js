const display = document.getElementById("display");
const buttons = document.querySelectorAll("[data-value]");
const equals = document.getElementById("equals");
const clear = document.getElementById("clear");

buttons.forEach(button => {
  button.addEventListener("click", () => {
    display.value += button.dataset.value;
  });
});

clear.addEventListener("click", () => {
  display.value = "";
});

equals.addEventListener("click", calculate);

function calculate() {
  const expression = display.value;

  if (!expression) return;

  // Allow only numbers, decimal points, spaces and calculator operators.
  if (!/^[0-9+\-*/.\s]+$/.test(expression)) {
    display.value = "Error";
    return;
  }

  try {
    const result = Function('"use strict"; return (' + expression + ')')();

    if (!Number.isFinite(result)) {
      display.value = "Error";
      return;
    }

    display.value = String(result);
  } catch {
    display.value = "Error";
  }
}

document.addEventListener("keydown", event => {
  if (/^[0-9.]$/.test(event.key) || ["+", "-", "*", "/"].includes(event.key)) {
    display.value += event.key;
  } else if (event.key === "Enter" || event.key === "=") {
    calculate();
  } else if (event.key === "Backspace") {
    display.value = display.value.slice(0, -1);
  } else if (event.key === "Escape") {
    display.value = "";
  }
});
