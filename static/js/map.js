function initDashboardMap() {
    const mapElement = document.getElementById('dashboard-map');
    if (!mapElement) return;

    const map = L.map('dashboard-map').setView([-25.4367, 31.9544], 13);

    L.tileLayer('https://tile.openstreetmap.org/{z}/{x}/{y}.png', {
        maxZoom: 19,
        attribution: '&copy; OpenStreetMap contributors',
        crossOrigin: true
    }).addTo(map);

    const rawReports = mapElement.dataset.reports;

    if (rawReports) {
        try {
            const reports = JSON.parse(rawReports);
            const validReports = reports.filter(
                item => item.lat !== null && item.lng !== null
            );

            if (validReports.length > 0) {
                const bounds = [];

                validReports.forEach(item => {
                    const marker = L.marker([item.lat, item.lng]).addTo(map);

                    marker.bindPopup(`
                        <div style="min-width:220px;">
                            <strong>${item.title}</strong><br>
                            <span>${item.type}</span><br>
                            <span>Status: ${item.status}</span><br>
                            <span>${item.area}</span>
                        </div>
                    `);

                    bounds.push([item.lat, item.lng]);
                });

                if (bounds.length > 1) {
                    map.fitBounds(bounds, { padding: [30, 30] });
                } else {
                    map.setView(bounds[0], 15);
                }

                return;
            }
        } catch (error) {
            console.error('Could not parse dashboard map reports:', error);
        }
    }

    L.marker([-25.4367, 31.9544]).addTo(map)
        .bindPopup('Masibekela Village')
        .openPopup();
}

function initReportMap() {
    const mapElement = document.getElementById('report-map');
    if (!mapElement) return;

    const defaultLat = -25.4367;
    const defaultLng = 31.9544;

    const map = L.map('report-map').setView([defaultLat, defaultLng], 14);

    L.tileLayer('https://tile.openstreetmap.org/{z}/{x}/{y}.png', {
        maxZoom: 19,
        attribution: '&copy; OpenStreetMap contributors',
        crossOrigin: true
    }).addTo(map);

    let marker = null;
    const latInput = document.getElementById('id_latitude');
    const lngInput = document.getElementById('id_longitude');
    const areaInput = document.getElementById('id_area_name');
    const coordsText = document.getElementById('selected-coords');

    map.on('click', function(e) {
        const { lat, lng } = e.latlng;

        if (marker) {
            marker.setLatLng([lat, lng]);
        } else {
            marker = L.marker([lat, lng]).addTo(map);
        }

        latInput.value = lat.toFixed(6);
        lngInput.value = lng.toFixed(6);
        coordsText.textContent = `${lat.toFixed(6)}, ${lng.toFixed(6)}`;

        if (areaInput && areaInput.value.trim() === '') {
            areaInput.value = `Pinned location: ${lat.toFixed(6)}, ${lng.toFixed(6)}`;
        }
    });
}

function initTrackMap() {
    const mapElement = document.getElementById('track-map');
    if (!mapElement) return;

    const latField = document.getElementById('track-lat');
    const lngField = document.getElementById('track-lng');

    if (!latField || !lngField) return;

    const lat = parseFloat(latField.value);
    const lng = parseFloat(lngField.value);

    if (isNaN(lat) || isNaN(lng)) {
        mapElement.innerHTML = '<p style="padding:16px;">No saved location for this report.</p>';
        return;
    }

    const map = L.map('track-map').setView([lat, lng], 15);

    L.tileLayer('https://tile.openstreetmap.org/{z}/{x}/{y}.png', {
        maxZoom: 19,
        attribution: '&copy; OpenStreetMap contributors',
        crossOrigin: true
    }).addTo(map);

    L.marker([lat, lng]).addTo(map)
        .bindPopup('Reported issue location')
        .openPopup();
}

document.addEventListener('DOMContentLoaded', function() {
    initDashboardMap();
    initReportMap();
    initTrackMap();
});