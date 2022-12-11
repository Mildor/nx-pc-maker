Cypress.Commands.add("login", ()=>{
  const username = 'admin'
  const password = 'admin'
  cy.visit('http://127.0.0.1:8000/pcMaker/login/')
  cy.get('input[name=username]').type(username)
  cy.get('input[name=password]').type(password)
  cy.get('form').submit()
})

beforeEach(() => {
  cy.login()
  cy.location('href').should('match', /http:\/\/127\.0\.0\.1:8000\/pcMaker\//i)
  cy.get('a[href*="/pcMaker/stockage/"]').click()
})

describe('CRUD CG', () => {

  it('create', () => {
    cy.get('input[id*="id_type"]').should("be.visible")
    cy.get('input[id*="id_type"]').type("TES")

    cy.get('input[id*="id_taille"]').should("be.visible")
    cy.get('input[id*="id_taille"]').type("9999")

    cy.get('button[type*="submit"]').should("be.visible")
    cy.get('button[type*="submit"]').click()

    cy.get('table').contains('td', 'TES').should('be.visible');
    cy.get('table').contains('td', '9999').should('be.visible');
  })

  it('Modify', ()=>{
    const parent = cy.get('tbody').contains('td', 'TES').parent();
    parent.children("td").contains("a", "Modifier").should("be.visible").click();

    cy.get('input[id*="id_type"]').should("be.visible").clear()
    cy.get('input[id*="id_type"]').type("MOD")

    cy.get('input[id*="id_taille"]').should("be.visible").clear()
    cy.get('input[id*="id_taille"]').type("8888")

    cy.get('button[type*="submit"]').should("be.visible")
    cy.get('button[type*="submit"]').contains("Modifier").click()

    cy.get('table').contains('td', 'MOD').should('be.visible');
    cy.get('table').contains('td', '8888').should('be.visible');
  })

  it('Delete', ()=>{
    const parent = cy.get('tbody').contains('td', 'MOD').parent();
    parent.children("td").contains("a", "Supprimer").should("be.visible").click();

    cy.get('table').contains('td', 'MOD').should('not.exist');
    cy.get('table').contains('td', '8888').should('not.exist');
  })

})
