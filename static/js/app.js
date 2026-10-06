function toggleSidebar(){
  document.getElementById("sidebar").classList.toggle("show");
}
function toggleGroup(id){
  const el=document.getElementById(id);
  if(el) el.classList.toggle("open");
}
function showTab(id){
  document.querySelectorAll(".tab-panel").forEach(x=>x.classList.add("hidden"));
  const el=document.getElementById(id);
  if(el) el.classList.remove("hidden");
}
function toggleCollapse(id){
  const el=document.getElementById(id);
  if(el) el.style.display=(el.style.display==="block"?"none":"block");
}
function openModal(){document.getElementById("modal")?.classList.remove("hidden")}
function closeModal(){document.getElementById("modal")?.classList.add("hidden")}

document.addEventListener("DOMContentLoaded",()=>{
  const input=document.getElementById("imageInput");
  const preview=document.getElementById("preview");
  if(input && preview){
    input.addEventListener("change",()=>{
      preview.innerHTML="";
      [...input.files].forEach(file=>{
        const reader=new FileReader();
        reader.onload=e=>{
          const img=document.createElement("img");
          img.src=e.target.result;
          img.alt=file.name;
          preview.appendChild(img);
        };
        reader.readAsDataURL(file);
      });
    });
  }
});
