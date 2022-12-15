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
    cy.get('[data-cy="stockage_Type"]').should("be.visible").type("TES")

    cy.get('[data-cy="stockage_Taille"]').should("be.visible").type("9999")

    cy.get('[data-cy="stockage_submit"]').should("be.visible").click()

    cy.get('table').contains('td', 'TES').should('be.visible');
    cy.get('table').contains('td', '9999').should('be.visible');
  })

  it('Modify', ()=>{
    const parent = cy.contains("tr","TES").children();
    parent.find('[data-cy="stockage_modifiy"]').click();

    cy.get('[data-cy="stockage_Type"]').should("be.visible").clear().type("CYP")

    cy.get('[data-cy="stockage_Taille"]').should("be.visible").clear().type("8888")

    cy.get('[data-cy="stockage_submit"]').should("be.visible").contains("Modifier").click()

    cy.get('table').contains('td', 'CYP').should('be.visible');
    cy.get('table').contains('td', '8888').should('be.visible');
  })

  it('Delete', ()=>{
    const parent = cy.contains("tr","CYP").children();
    parent.find('[data-cy="stockage_delete"]').click();

    cy.get('table').contains('td', 'CYP').should('not.exist');
    cy.get('table').contains('td', '8888').should('not.exist');
  })

})
