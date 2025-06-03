document.addEventListener("DOMContentLoaded", function() {
    const mapSelector = document.getElementById("mapSelector");
    const mapIframe = document.getElementById("mapIframe");
    mapSelector.addEventListener("change", function() {
        const selectedMap = mapSelector.value;
        mapIframe.src = "maps/" + selectedMap;
    });
});