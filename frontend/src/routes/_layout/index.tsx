import { createFileRoute, Link } from "@tanstack/react-router"

import { Button } from "@/components/ui/button"

export const Route = createFileRoute("/_layout/")({
  component: Home,
  head: () => ({
    meta: [
      {
        title: "Home - App",
      },
    ],
  }),
})

function Home() {
  return (
    <div className="flex flex-col gap-4">
      <div>
        <h1 className="text-2xl font-bold tracking-tight">App</h1>
        <p className="text-muted-foreground">
          One-line description of who this is for and what it does.
        </p>
      </div>
      <div>
        <Button asChild>
          <Link to="/items">Go to Items</Link>
        </Button>
      </div>
    </div>
  )
}
