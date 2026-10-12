const menu = document.querySelector('.menu-toggle');
const mobile = document.querySelector('#mobile-nav');
function closeMenu(){mobile.hidden=true;menu.setAttribute('aria-expanded','false');menu.textContent='MENU';}
menu.addEventListener('click',()=>{mobile.hidden=!mobile.hidden;menu.setAttribute('aria-expanded',String(!mobile.hidden));menu.textContent=mobile.hidden?'MENU':'CLOSE';});
document.addEventListener('keydown',event=>{if(event.key==='Escape'&&!mobile.hidden){closeMenu();menu.focus();}});
const filters = [...document.querySelectorAll('[data-filter]')];
const search = document.querySelector('#project-search');
const more = document.querySelector('#load-more');
let activeCategory='all', limit=24;
function filterWork(category){
  if(!['all','brand','corporate','event','media','live'].includes(category))category='all';
  activeCategory=category;
  filters.forEach(button=>button.setAttribute('aria-pressed',String(button.dataset.filter===category)));
  const query=(search?.value||'').toLocaleLowerCase().replace(/\s+/g,'');
  let count=0;
  document.querySelectorAll('.work-tile').forEach(tile=>{
    const match=(category==='all'||tile.dataset.category===category)&&tile.dataset.search.toLocaleLowerCase().replace(/\s+/g,'').includes(query);
    if(match)count++;
    tile.hidden=!match||count>limit;
  });
  const status=document.querySelector('#result-count');if(status)status.textContent=count+(count===1?' PROJECT':' PROJECTS');
  if(more){more.hidden=count<=limit;more.textContent=`MORE PROJECTS (${Math.min(limit,count)} / ${count})`;}
  const empty=document.querySelector('#empty-results');if(empty)empty.hidden=count!==0;
}
if(filters.length){
  const params=new URLSearchParams(location.search);
  if(search)search.value=params.get('q')||'';
  filterWork(params.get('category')||'all');
  function updateUrl(){const url=new URL(location.href);if(activeCategory==='all')url.searchParams.delete('category');else url.searchParams.set('category',activeCategory);if(search.value)url.searchParams.set('q',search.value);else url.searchParams.delete('q');history.replaceState(null,'',url);}
  filters.forEach(button=>button.addEventListener('click',()=>{limit=24;filterWork(button.dataset.filter);updateUrl();}));
  search?.addEventListener('input',()=>{limit=24;filterWork(activeCategory);updateUrl();});
  more?.addEventListener('click',()=>{const previous=limit;limit+=24;filterWork(activeCategory);[...document.querySelectorAll('.work-tile:not([hidden])')][previous]?.focus({preventScroll:true});});
}
