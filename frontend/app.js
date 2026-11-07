const API = ''; // Same-origin Nginx proxy routes API calls to the in-cluster product service.
const fallback = [
{id:'p1',name:'Cloud Runner Sneakers',category:'Footwear',price:89,color:'#dff7ee',emoji:'👟',badge:'BESTSELLER'},
{id:'p2',name:'Everyday Tote',category:'Accessories',price:42,color:'#fff0d9',emoji:'👜',badge:'NEW'},
{id:'p3',name:'Studio Headphones',category:'Electronics',price:129,color:'#eee7ff',emoji:'🎧',badge:'TOP RATED'},
{id:'p4',name:'Ceramic Travel Mug',category:'Lifestyle',price:28,color:'#ffe6e9',emoji:'☕',badge:'ECO PICK'},
{id:'p5',name:'Weekend Camera',category:'Electronics',price:219,color:'#e4f0ff',emoji:'📷',badge:'LIMITED'},
{id:'p6',name:'Soft Knit Hoodie',category:'Apparel',price:74,color:'#f4e8ff',emoji:'🧥',badge:'TRENDING'}];
let products=fallback, cart=[];
async function loadProducts(){try{const r=await fetch('/api/products');if(r.ok){const data=await r.json();if(Array.isArray(data)&&data.length)products=data;}}catch(e){}renderProducts()}
function renderProducts(){const q=(document.querySelector('#search')?.value||'').toLowerCase(),cat=document.querySelector('#category')?.value||'All';const list=products.filter(p=>(cat==='All'||p.category===cat)&&(p.name.toLowerCase().includes(q)||p.category.toLowerCase().includes(q)));document.querySelector('#products').innerHTML=list.length?list.map(p=>`<article class="product-card"><div class="product-art" style="background:${p.color||'#e3f8ee'}"><span class="badge">${p.badge||'JUST FOR YOU'}</span><span class="product-emoji">${p.emoji||'✨'}</span></div><div class="product-info"><span class="product-category">${p.category}</span><h3>${p.name}</h3><div class="product-bottom"><span class="price">$${Number(p.price).toFixed(2)}</span><button class="add-btn" aria-label="Add ${p.name}" onclick="addToCart('${p.id}')">＋</button></div></div></article>`).join(''):'<p>No finds yet. Try another search.</p>'}
function addToCart(id){const p=products.find(x=>x.id===id);if(!p)return;cart.push(p);document.querySelector('#cart-count').textContent=cart.length;toast(`${p.name} added to your bag ✦`)}
function showCart(){if(!cart.length){toast('Your bag is waiting for something lovely.');return}const total=cart.reduce((s,p)=>s+Number(p.price),0);toast(`${cart.length} item(s) · $${total.toFixed(2)} — demo bag only`)}
function subscribe(e){e.preventDefault();document.querySelector('#subscribe-note').textContent='You’re on the list — stay bright! ✦';e.target.reset()}
function toast(msg){const t=document.querySelector('#toast');t.textContent=msg;t.classList.add('show');clearTimeout(window.toastTimer);window.toastTimer=setTimeout(()=>t.classList.remove('show'),2600)}
loadProducts();
