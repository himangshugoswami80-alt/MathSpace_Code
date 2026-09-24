import './globals.css';
import Link from 'next/link';
export default function RootLayout({children}:{children:React.ReactNode}){
 return <html lang="en"><body><header className="border-b bg-white"><nav className="mx-auto flex max-w-6xl items-center justify-between p-4"><Link href="/" className="text-xl font-bold">MathSpace</Link><div className="flex gap-4 text-sm"><Link href="/learn">Learn</Link><Link href="/ai-tutor">AI Tutor</Link><Link href="/graph">Graph</Link></div></nav></header>{children}</body></html>
}