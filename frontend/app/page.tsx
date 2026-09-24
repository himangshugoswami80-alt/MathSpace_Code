import Link from 'next/link';
export default function Home(){
 return <main className="mx-auto max-w-6xl px-6 py-20">
  <section className="card p-10"><p className="mb-3 text-sm font-semibold text-violet-600">AI Mathematics Intelligence Platform</p>
  <h1 className="max-w-3xl text-5xl font-bold tracking-tight">See the mathematics behind the real world.</h1>
  <p className="mt-5 max-w-2xl text-lg text-gray-600">Concept → Formula → Model → Simulation → Visualization</p>
  <div className="mt-8 flex gap-3"><Link className="rounded-xl bg-violet-600 px-5 py-3 text-white" href="/learn">Start Learning</Link><Link className="rounded-xl border px-5 py-3" href="/ai-tutor">Ask AI Tutor</Link></div>
  </section>
  <div className="mt-8 grid gap-5 md:grid-cols-3">
   {['Interactive Mathematics','AI Tutor','Real-world Modelling'].map(x=><div className="card p-6" key={x}><h2 className="font-semibold">{x}</h2><p className="mt-2 text-sm text-gray-600">Build concepts, calculations and experiments in one workspace.</p></div>)}
  </div>
 </main>
}