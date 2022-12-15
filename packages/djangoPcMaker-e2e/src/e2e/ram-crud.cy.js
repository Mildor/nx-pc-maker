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
  cy.get('a[href*="/pcMaker/ram/"]').click()
})

describe('CRUD ram', () => {

  it('create', () => {
    cy.get('[data-cy="ram_Marque"]').should("be.visible").type("TEST")

    cy.get('[data-cy="ram_Frequence"]').should("be.visible").type("0000")

    cy.get('[data-cy="ram_Taille"]').should("be.visible").type("1")

    cy.get('[data-cy="ram_submit"]').should("be.visible").click()

    cy.get('table').contains('td', 'TEST').should('be.visible');
    cy.get('table').contains('td', '0000').should('be.visible');
    cy.get('table').contains('td', '1').should('be.visible');
  })

  it('Modify', ()=>{
    const parent = cy.contains("tr","TEST").children();
    parent.find('[data-cy="ram_modify"]').click();

    cy.get('[data-cy="ram_Marque"]').should("be.visible").clear().type("CYP")

    cy.get('[data-cy="ram_Frequence"]').should("be.visible").clear().type("1000")

    cy.get('[data-cy="ram_Taille"]').should("be.visible").clear().type("11")

    cy.get('[data-cy="ram_submit"]').should("be.visible").contains("Modifier").click()

    cy.get('table').contains('td', 'CYP').should('be.visible');
    cy.get('table').contains('td', '1000').should('be.visible');
    cy.get('table').contains('td', '11').should('be.visible');
  })

  it('Delete', ()=>{
    const parent = cy.contains("tr","CYP").children();
    parent.find('[data-cy="ram_delete"]').click();

    cy.get('table').contains('td', 'CYP').should('not.exist');
    cy.get('table').contains('td', '1000').should('not.exist');
    cy.get('table').contains('td', '11').should('not.exist');
  })

})
