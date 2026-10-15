import { expect, test } from "@playwright/test"

// Example e2e for the template's Items resource. Replace with the problem's
// demo script: one test per demo step, driven like a user would.

const uniqueTitle = () => `Item ${Math.random().toString(36).slice(2, 8)}`

test.beforeEach(async ({ page }) => {
  await page.goto("/items")
})

test("create an item", async ({ page }) => {
  const title = uniqueTitle()
  await page.getByRole("button", { name: "Add Item" }).click()
  await page.getByLabel("Title").fill(title)
  await page.getByRole("button", { name: "Save" }).click()

  await expect(page.getByText("Item created successfully")).toBeVisible()
  await expect(page.getByText(title)).toBeVisible()
})

test("title is required", async ({ page }) => {
  await page.getByRole("button", { name: "Add Item" }).click()
  await page.getByLabel("Title").fill("")
  await page.getByLabel("Title").blur()

  await expect(page.getByText("Title is required")).toBeVisible()
})

test("edit then delete an item", async ({ page }) => {
  const title = uniqueTitle()
  await page.getByRole("button", { name: "Add Item" }).click()
  await page.getByLabel("Title").fill(title)
  await page.getByRole("button", { name: "Save" }).click()
  await expect(page.getByRole("dialog")).not.toBeVisible()

  const row = page.getByRole("row").filter({ hasText: title })
  await row.getByRole("button").last().click()
  await page.getByRole("menuitem", { name: "Edit Item" }).click()
  const updated = uniqueTitle()
  await page.getByLabel("Title").fill(updated)
  await page.getByRole("button", { name: "Save" }).click()
  await expect(page.getByText(updated)).toBeVisible()

  const updatedRow = page.getByRole("row").filter({ hasText: updated })
  await updatedRow.getByRole("button").last().click()
  await page.getByRole("menuitem", { name: "Delete Item" }).click()
  await page.getByRole("button", { name: "Delete" }).click()
  await expect(page.getByText(updated)).not.toBeVisible()
})
