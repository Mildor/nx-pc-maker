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
  cy.get('a[href*="/pcMaker/processeur/"]').click()
})


describe('CRUD proc', () => {
  it('Create', () => {
    cy.get('input[id*="id_marque"]').should("be.visible")
    cy.get('input[id*="id_marque"]').type("Test")

    cy.get('input[id*="id_categorie"]').should("be.visible")
    cy.get('input[id*="id_categorie"]').type("Cy")

    cy.get('input[id*="id_modele"]').should("be.visible")
    cy.get('input[id*="id_modele"]').type("ress")

    cy.get('button[type*="submit"]').should("be.visible")
    cy.get('button[type*="submit"]').click()

    cy.get('tbody').contains('td', 'Test').should('be.visible');
    cy.get('tbody').contains('td', 'Cy').should('be.visible');
    cy.get('tbody').contains('td', 'ress').should('be.visible');
  })

  it('Modify', () => {
    const parent = cy.get('tbody').contains('td', 'Test').parent();
    parent.children("td").contains("a", "Modifier").should("be.visible").click();

    cy.get('input[id*="id_marque"]').should("be.visible").clear()
    cy.get('input[id*="id_marque"]').type("Mod")

    cy.get('input[id*="id_categorie"]').should("be.visible").clear()
    cy.get('input[id*="id_categorie"]').type("If")

    cy.get('input[id*="id_modele"]').should("be.visible").clear()
    cy.get('input[id*="id_modele"]').type("y")

    cy.get('button[type*="submit"]').should("be.visible")
    cy.get('button[type*="submit"]').click()

    cy.get('tbody').contains('td', 'Mod').should('be.visible');
    cy.get('tbody').contains('td', 'If').should('be.visible');
    cy.get('tbody').contains('td', 'y').should('be.visible');
  })

  it('Delete', () => {
    const parent = cy.get('tbody').contains('td', 'Mod').parent();
    parent.children("td").contains("a", "Supprimer").should("be.visible").click();

    cy.get('table').contains('td', 'Mod').should('not.exist');
    cy.get('table').contains('td', 'If').should('not.exist');
    cy.get('table').contains('td', 'y').should('not.exist');
  })
})
