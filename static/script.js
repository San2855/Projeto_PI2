// Seleciona o elemento do formulário
const form = document.querySelector('form');

// Seleciona o botão de envio
const submitBtn = document.querySelector('#submitBtn');

// Desativa o botão de envio quando a página é carregada
submitBtn.disabled = true;

// Adiciona um ouvinte de eventos ao campo de entrada de e-mail
form.email.addEventListener('input', () => {
  // Verifica se o campo de entrada de e-mail contém um valor válido
  if (form.email.validity.valid) {
    // Ativa o botão de envio se todos os campos de entrada forem válidos
    if (form.nome.validity.valid && form.data.validity.valid && form.hora.validity.valid) {
      submitBtn.disabled = false;
    }
  } else {
    submitBtn.disabled = true;
  }
});

// Adiciona um ouvinte de eventos ao campo de entrada de nome
form.nome.addEventListener('input', () => {
  // Verifica se o campo de entrada de nome contém um valor válido
  if (form.nome.validity.valid) {
    // Ativa o botão de envio se todos os campos de entrada forem válidos
    if (form.email.validity.valid && form.data.validity.valid && form.hora.validity.valid) {
      submitBtn.disabled = false;
    }
  } else {
    submitBtn.disabled = true;
  }
});

// Adiciona um ouvinte de eventos ao campo de entrada de data
form.data.addEventListener('input', () => {
  // Verifica se o campo de entrada de data contém um valor válido
  if (form.data.validity.valid) {
    // Ativa o botão de envio se todos os campos de entrada forem válidos
    if (form.email.validity.valid && form.nome.validity.valid && form.hora.validity.valid) {
      submitBtn.disabled = false;
    }
  } else {
    submitBtn.disabled = true;
  }
});
