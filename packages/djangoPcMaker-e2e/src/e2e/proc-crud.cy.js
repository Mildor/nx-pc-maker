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
    cy.get('[data-cy="processeur_Marque"]').should("be.visible").type("Test")

    cy.get('[data-cy="processeur_Categorie"]').should("be.visible").type("Cy")

    cy.get('[data-cy="processeur_Modele"]').should("be.visible").type("ress")

    cy.get('[data-cy="processeur_submit"]').should("be.visible").click()

    cy.get('tbody').contains('td', 'Test').should('be.visible');
    cy.get('tbody').contains('td', 'Cy').should('be.visible');
    cy.get('tbody').contains('td', 'ress').should('be.visible');
  })

  it('Modify', () => {
    const parent = cy.contains("tr","Test").children();
    parent.find('[data-cy="processeur_modify"]').click();

    cy.get('[data-cy="processeur_Marque"]').should("be.visible").clear().type("jai")

    cy.get('[data-cy="processeur_Categorie"]').should("be.visible").clear().type("ch")

    cy.get('[data-cy="processeur_Modele"]').should("be.visible").clear().type("a")

    cy.get('[data-cy="processeur_submit"]').should("be.visible").click()

    cy.get('tbody').contains('td', 'jai').should('be.visible');
    cy.get('tbody').contains('td', 'ch').should('be.visible');
    cy.get('tbody').contains('td', 'a').should('be.visible');
  })

  it('Delete', () => {
    const parent = cy.contains("tr","jai").children();
    parent.find('[data-cy="processeur_delete"]').click();

    cy.get('table').contains('td', 'jai').should('not.exist');
    cy.get('table').contains('td', 'ch').should('not.exist');
    cy.get('table').contains('td', 'a').should('not.exist');
  })
})
