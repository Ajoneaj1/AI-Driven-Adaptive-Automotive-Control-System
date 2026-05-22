async function predictSettings() {
    const road = document.getElementById('road').value;
    const temp = document.getElementById('temp').value;
    const speed = document.getElementById('speed').value;
    const rain = document.getElementById('rain').value;

    const response = await fetch('http://127.0.0.1:5000/predict', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({
            road_roughness: road,
            ambient_temp: temp,
            speed: speed,
            is_raining: rain
        })
    });

    const data = await response.json();

    document.getElementById('suspension').innerText = data.suspension_setting;
    document.getElementById('ac').innerText = data.ac_level;
    document.getElementById('tire').innerText = data.tire_pressure_adjust;
    document.getElementById('speedAdjust').innerText = data.speed_limit_adjust;
}