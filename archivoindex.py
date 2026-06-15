html_content = """<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Gente Saludable - Presentación Ejecutiva</title>
    
    <!-- Reveal.js CSS -->
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/reveal.js/4.3.1/reveal.min.css">
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/reveal.js/4.3.1/theme/white.min.css">
    
    <!-- Font Awesome -->
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">
    
    <!-- Google Fonts -->
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;600;700&family=Merriweather:ital,wght@0,300;0,700;1,400&display=swap" rel="stylesheet">
    
    <style>
        :root {
            /* Colores Base */
            --bg-light: #F7F4EF;
            --bg-med: #EAE2D6;
            --text-main: #2C2621;
            
            /* Colores Corporativos */
            --corp-blue: #225792;
            --corp-green: #91BF2D;
            --corp-gray: #656565;
            --corp-white: #FFFFFF;
            
            /* Alertas */
            --alert-red: #A04A3A;
            --alert-orange: #F29C38;
            --alert-red-bright: #D32F2F; /* Para impactos económicos urgentes */
        }

        /* Tipografías Globales Reveal */
        .reveal {
            font-family: 'Inter', sans-serif;
            color: var(--text-main);
            background-color: var(--bg-light);
        }

        .reveal h1, .reveal h2, .reveal h3, .reveal h4, .reveal h5, .reveal h6 {
            font-family: 'Merriweather', serif;
            color: var(--corp-blue);
            text-transform: none;
            letter-spacing: normal;
        }

        .reveal h1 { font-weight: 700; font-size: 3.5em; }
        .reveal h2 { font-weight: 700; font-size: 2.5em; margin-bottom: 20px; }
        .reveal p, .reveal li { font-size: 1.2rem; line-height: 1.4; }
        
        .reveal a { color: var(--corp-blue); }
        .reveal a:hover { color: var(--corp-green); }

        sup a {
            color: var(--alert-orange);
            font-weight: bold;
            text-decoration: none;
            font-size: 0.6em;
        }

        /* Utilidades de Color de Texto */
        .text-blue { color: var(--corp-blue) !important; }
        .text-green { color: var(--corp-green) !important; }
        .text-red { color: var(--alert-red-bright) !important; font-weight: bold; }
        .text-orange { color: var(--alert-orange) !important; }

        /* Tarjetas Académicas */
        .academic-card {
            background-color: var(--corp-white);
            border-left: 8px solid var(--corp-blue);
            padding: 20px 30px;
            box-shadow: 0 4px 15px rgba(0,0,0,0.05);
            border-radius: 4px;
            text-align: left;
            margin-bottom: 20px;
        }
        .academic-card h3 {
            font-size: 1.5rem;
            margin-top: 0;
            color: var(--text-main);
        }

        /* Slide 1 - Hero */
        .hero-box {
            background: rgba(255, 255, 255, 0.85);
            padding: 50px;
            border-radius: 10px;
            display: inline-block;
            max-width: 1200px;
            box-shadow: 0 10px 30px rgba(0,0,0,0.2);
            backdrop-filter: blur(5px);
        }
        .hero-logo {
            max-width: 400px;
            margin-bottom: 30px;
        }
        .hero-title {
            font-size: 4rem !important;
            margin-bottom: 20px !important;
        }
        .hero-subtitle {
            font-size: 1.8rem;
            color: var(--corp-gray);
            font-family: 'Inter', sans-serif;
            font-weight: 300;
        }

        /* Slide 2 - Grid de Pérdidas */
        .losses-grid {
            display: grid;
            grid-template-columns: repeat(5, 1fr);
            gap: 15px;
            margin-top: 30px;
        }
        .loss-item {
            background: var(--bg-med);
            border: 2px solid var(--corp-blue);
            border-radius: 8px;
            padding: 15px;
            cursor: pointer;
            transition: all 0.3s ease;
            display: flex;
            align-items: center;
            justify-content: center;
            min-height: 120px;
            position: relative;
            overflow: hidden;
        }
        .loss-item:hover {
            transform: translateY(-5px);
            box-shadow: 0 5px 15px rgba(34, 87, 146, 0.3);
            background: var(--corp-blue);
            color: white;
        }
        .loss-item h4 {
            margin: 0;
            font-size: 1.1rem;
            text-align: center;
            transition: color 0.3s ease;
        }
        .loss-item:hover h4 { color: white; }
        
        .loss-detail-overlay {
            position: absolute;
            top: 0; left: 0; right: 0; bottom: 0;
            background: rgba(255,255,255,0.95);
            z-index: 10;
            display: none;
            flex-direction: column;
            justify-content: center;
            align-items: center;
            padding: 40px;
            border-radius: 10px;
            box-shadow: 0 10px 40px rgba(0,0,0,0.2);
            border: 3px solid var(--corp-blue);
        }
        .loss-detail-overlay.active { display: flex; }
        .loss-detail-overlay .close-btn {
            position: absolute;
            top: 15px; right: 20px;
            font-size: 2rem;
            cursor: pointer;
            color: var(--corp-gray);
        }
        .loss-detail-overlay .close-btn:hover { color: var(--alert-red); }

        /* Slide 3 - Iceberg */
        .iceberg-container {
            position: relative;
            width: 100%;
            height: 700px;
        }
        .iceberg-top {
            position: absolute;
            top: 0; left: 0; right: 0;
            height: 40%;
            background: rgba(255,255,255,0.85);
            padding: 20px;
            border-radius: 10px;
        }
        .iceberg-bottom {
            position: absolute;
            bottom: 0; left: 0; right: 0;
            height: 55%;
            background: rgba(255,255,255,0.9);
            padding: 20px;
            border-radius: 10px;
        }
        .iceberg-cover {
            position: absolute;
            bottom: 0; left: 0; right: 0;
            height: 60%;
            background: var(--corp-blue);
            display: flex;
            align-items: center;
            justify-content: center;
            z-index: 5;
            border-radius: 10px;
        }
        .btn-reveal {
            background: var(--corp-green);
            color: white;
            border: none;
            padding: 15px 30px;
            font-size: 1.5rem;
            border-radius: 5px;
            cursor: pointer;
            font-weight: bold;
            box-shadow: 0 4px 10px rgba(0,0,0,0.3);
            transition: background 0.3s ease;
        }
        .btn-reveal:hover { background: #7ba325; }
        
        .iceberg-content {
            display: grid;
            grid-template-columns: 1fr 1fr;
            gap: 20px;
            text-align: left;
            font-size: 0.9rem;
        }
        .iceberg-content ul { padding-left: 20px; margin-top: 5px; }
        .iceberg-content li { margin-bottom: 5px; }

        /* Slide 4 - Cuadrantes */
        .quadrants-grid {
            display: grid;
            grid-template-columns: 1fr 1fr;
            gap: 30px;
        }
        .quadrant {
            background: white;
            border-radius: 8px;
            padding: 20px;
            box-shadow: 0 4px 15px rgba(0,0,0,0.05);
            border-top: 5px solid;
            text-align: left;
        }
        .quadrant-tl { border-color: var(--alert-red); }
        .quadrant-tr { border-color: var(--corp-blue); }
        .quadrant-bl { border-color: var(--alert-orange); }
        .quadrant-br { border-color: var(--corp-green); }
        .quadrant h3 { font-size: 1.4rem; margin-top: 0; display: flex; align-items: center; gap: 10px; }
        .quadrant ul { font-size: 1rem; margin-bottom: 0; padding-left: 20px; }
        .quadrant li { margin-bottom: 8px; }

        /* Slide 5 - Red Neuronal Clínico */
        .clinical-mapping {
            display: grid;
            grid-template-columns: 250px 1fr 350px;
            gap: 20px;
            height: 650px;
            margin-top: 20px;
        }
        .diagnosis-list {
            display: flex;
            flex-direction: column;
            gap: 10px;
            overflow-y: auto;
            padding-right: 10px;
        }
        .diag-btn {
            background: var(--bg-med);
            border: 1px solid #ccc;
            padding: 15px;
            text-align: left;
            border-radius: 5px;
            cursor: pointer;
            font-family: 'Inter', sans-serif;
            font-weight: 600;
            transition: all 0.2s;
        }
        .diag-btn:hover, .diag-btn.active {
            background: var(--corp-blue);
            color: white;
            border-color: var(--corp-blue);
        }
        .symptoms-display {
            background: white;
            padding: 30px;
            border-radius: 8px;
            box-shadow: 0 4px 15px rgba(0,0,0,0.05);
            text-align: left;
            border-left: 5px solid var(--corp-blue);
        }
        .losses-list-col {
            background: var(--bg-med);
            padding: 15px;
            border-radius: 8px;
            display: flex;
            flex-direction: column;
            gap: 8px;
        }
        .loss-node {
            background: white;
            padding: 10px;
            border-radius: 4px;
            font-size: 0.9rem;
            display: flex;
            justify-content: space-between;
            align-items: center;
            border-left: 4px solid transparent;
            transition: all 0.5s ease;
        }
        .loss-node.highlighted {
            background: #fdf2f0;
            border-left-color: var(--alert-red);
            box-shadow: 0 2px 8px rgba(160, 74, 58, 0.3);
        }
        .loss-badge {
            background: var(--alert-red);
            color: white;
            font-size: 0.75rem;
            padding: 3px 8px;
            border-radius: 12px;
            font-weight: bold;
            opacity: 0;
            transform: scale(0.8);
            transition: all 0.5s ease;
        }
        .loss-node.highlighted .loss-badge {
            opacity: 1;
            transform: scale(1);
        }

        /* Slide 6 - Dominó */
        .domino-track {
            display: flex;
            justify-content: center;
            align-items: flex-end;
            height: 300px;
            margin: 50px 0;
            gap: 15px;
            perspective: 1000px;
        }
        .domino {
            width: 100px;
            height: 220px;
            background: var(--corp-blue);
            color: white;
            border-radius: 5px;
            display: flex;
            align-items: center;
            justify-content: center;
            text-align: center;
            padding: 10px;
            font-size: 1rem;
            font-weight: bold;
            cursor: pointer;
            box-shadow: inset -5px 0 10px rgba(0,0,0,0.2), 5px 5px 15px rgba(0,0,0,0.3);
            border: 2px solid white;
            transform-origin: bottom right;
        }
        .domino:last-child {
            background: var(--alert-red);
            width: 140px;
        }
        .domino-desc {
            font-size: 1.1rem;
            text-align: left;
            background: white;
            padding: 20px;
            border-radius: 8px;
            min-height: 150px;
        }

        /* Slide 7 - Pilares */
        .pillars-grid {
            display: grid;
            grid-template-columns: 1fr 1fr;
            gap: 20px;
        }
        .pillar-card {
            background: white;
            border-top: 5px solid var(--corp-green);
            padding: 25px;
            border-radius: 8px;
            box-shadow: 0 4px 15px rgba(0,0,0,0.05);
            text-align: left;
        }
        .pillar-card h3 { color: var(--corp-blue); font-size: 1.4rem; margin-top: 0;}
        .pillar-card p, .pillar-card li { font-size: 1rem; }

        /* Slide 8 - Tabla */
        .styled-table {
            width: 100%;
            border-collapse: collapse;
            margin: 25px 0;
            font-size: 0.9em;
            font-family: 'Inter', sans-serif;
            box-shadow: 0 0 20px rgba(0, 0, 0, 0.05);
            background: white;
        }
        .styled-table thead tr {
            background-color: var(--corp-blue);
            color: #ffffff;
            text-align: left;
        }
        .styled-table th, .styled-table td {
            padding: 15px 20px;
            border-bottom: 1px solid #dddddd;
            text-align: left;
        }
        .styled-table tbody tr:last-of-type {
            border-bottom: 2px solid var(--corp-blue);
        }
        .styled-table tbody tr:nth-of-type(even) {
            background-color: #f9f9f9;
        }

        /* Slide 9 - Ética */
        .ethics-list {
            list-style: none;
            padding: 0;
            text-align: left;
            display: inline-block;
            font-size: 1.5rem;
        }
        .ethics-list li {
            margin-bottom: 15px;
            display: flex;
            align-items: center;
            gap: 15px;
        }
        .ethics-no { color: var(--alert-red); font-weight: bold; }
        .ethics-yes { color: var(--corp-green); font-weight: bold; }

        .bonus-box {
            background: var(--corp-blue);
            color: white;
            padding: 30px;
            border-radius: 10px;
            margin-top: 40px;
            text-align: left;
        }
        .bonus-box h3 { color: white; margin-top:0; }

        /* Slide 10 - Contacto */
        .contact-box {
            background: white;
            padding: 60px;
            border-radius: 10px;
            box-shadow: 0 10px 30px rgba(0,0,0,0.1);
            display: inline-block;
        }
        .contact-box img { max-width: 300px; margin-bottom: 30px; }
        .contact-info {
            font-size: 1.8rem;
            color: var(--corp-blue);
            margin-top: 30px;
        }

        /* Slide 11 - Referencias */
        .refs-container {
            text-align: left;
            font-size: 0.85rem;
            height: 700px;
            overflow-y: auto;
            padding-right: 20px;
        }
        .refs-container li { margin-bottom: 12px; }

        /* Ajustes pequeños */
        .reveal .slide-number {
            color: var(--corp-blue);
            background-color: transparent;
            font-weight: bold;
        }
    </style>
</head>
<body>

    <div class="reveal">
        <div class="slides">

            <!-- Slide 01: El Gancho (Hero) -->
            <section data-background-video="video barco.mp4" data-background-video-loop="true" data-background-video-muted="true">
                <div class="hero-box">
                    <img src="logofblancovector.jpg" alt="Gente Saludable Logo" class="hero-logo">
                    <h1 class="hero-title" style="opacity: 0;">El costo invisible de navegar</h1>
                    <p class="hero-subtitle">Cómo la <span class="text-green" style="font-weight:600;">SALUD MENTAL</span> de la tripulación impacta directamente en la seguridad, productividad y rentabilidad neta de la flota en la Hidrovía.</p>
                </div>
            </section>

            <!-- Slide 02: Top 10 Pérdidas -->
            <section>
                <h2>Top 10 de Pérdidas Ocultas</h2>
                <p>Por el Factor Humano y Salud Mental en Navieras. (Click para ampliar)</p>
                
                <div class="losses-grid">
                    <!-- Cards will be generated via HTML/JS -->
                    <div class="loss-item" onclick="openLossDetail(1)"><h4>1. Accidentes por Fatiga <sup><a href="#/10">1</a></sup></h4></div>
                    <div class="loss-item" onclick="openLossDetail(2)"><h4>2. Absentismo Médico <sup><a href="#/10">2</a></sup></h4></div>
                    <div class="loss-item" onclick="openLossDetail(3)"><h4>3. Alta Rotación <sup><a href="#/10">3</a></sup></h4></div>
                    <div class="loss-item" onclick="openLossDetail(4)"><h4>4. Errores Sub-notificados <sup><a href="#/10">4</a></sup></h4></div>
                    <div class="loss-item" onclick="openLossDetail(5)"><h4>5. Daño a la Carga <sup><a href="#/10">5</a></sup></h4></div>
                    <div class="loss-item" onclick="openLossDetail(6)"><h4>6. Sanciones Normativas <sup><a href="#/10">6</a></sup></h4></div>
                    <div class="loss-item" onclick="openLossDetail(7)"><h4>7. Baja Eficiencia (Presentismo) <sup><a href="#/10">7</a></sup></h4></div>
                    <div class="loss-item" onclick="openLossDetail(8)"><h4>8. Conflictos Sindicales <sup><a href="#/10">8</a></sup></h4></div>
                    <div class="loss-item" onclick="openLossDetail(9)"><h4>9. Pérdida de Contratos <sup><a href="#/10">1</a></sup></h4></div>
                    <div class="loss-item" onclick="openLossDetail(10)"><h4>10. Litigios Laborales <sup><a href="#/10">9</a></sup></h4></div>
                </div>

                <!-- Overlay para detalle (oculto por defecto) -->
                <div class="loss-detail-overlay" id="lossOverlay">
                    <i class="fa-solid fa-xmark close-btn" onclick="closeLossDetail()"></i>
                    <h2 id="lossTitle" class="text-blue" style="margin-bottom:10px;">Título</h2>
                    <div class="academic-card" style="width: 80%; max-width: 1000px; font-size: 1.3rem;">
                        <p id="lossDesc">Descripción aquí.</p>
                        <hr style="border:0; border-top:1px solid #ccc; margin: 20px 0;">
                        <p><strong>Impacto económico:</strong> <span id="lossImpact" class="text-red">USD $0</span></p>
                    </div>
                </div>
            </section>

            <!-- Slide 03: Paradigma del Iceberg -->
            <section data-background-image="iceberg presentacion.png" data-background-size="cover">
                <div class="iceberg-container">
                    <div class="iceberg-top">
                        <h3 class="text-blue" style="margin:0;"><i class="fa-solid fa-triangle-exclamation"></i> La Punta del Iceberg (Lo Visible)</h3>
                        <p style="font-size: 1rem; margin-top:5px; color: var(--corp-gray);">Gestionar esta parte es actuar de forma <strong>reactiva</strong>.</p>
                        <div class="iceberg-content">
                            <ul>
                                <li>Accidentes y Siniestros Graves</li>
                                <li>Renuncias y Alta Rotación</li>
                                <li>Multas y Sanciones</li>
                                <li>Daños a la Carga y Maquinaria</li>
                            </ul>
                            <ul>
                                <li>Absentismo Médico Prolongado</li>
                                <li>Litigios y Demandas Laborales</li>
                                <li>Paralización de la Flota</li>
                            </ul>
                        </div>
                    </div>

                    <div class="iceberg-bottom">
                        <h3 class="text-blue" style="margin:0;"><i class="fa-solid fa-water"></i> La Base del Iceberg (Lo Oculto)</h3>
                        <p style="font-size: 1rem; margin-top:5px; color: var(--corp-gray);">Gestionar esta parte es actuar de forma <strong>preventiva</strong>.</p>
                        <div class="iceberg-content">
                            <ul>
                                <li>Fatiga Crónica y Déficit de Sueño</li>
                                <li>Estrés Laboral y Burnout</li>
                                <li>Presentismo y Apatía</li>
                                <li>Errores Sub-notificados</li>
                            </ul>
                            <ul>
                                <li>Déficit de Apoyo Social / Aislamiento</li>
                                <li>Trastornos Psicosomáticos</li>
                                <li>Sobrecarga Emocional</li>
                                <li>Demandas Psicológicas</li>
                            </ul>
                        </div>
                    </div>

                    <div class="iceberg-cover" id="icebergCover">
                        <div style="text-align: center; color: white; width: 80%;">
                            <h2 style="color:white; text-shadow: 2px 2px 4px rgba(0,0,0,0.5);">"La mayoría interviene cuando el problema ya emergió..."</h2>
                            <p style="font-size: 1.5rem; text-shadow: 1px 1px 3px rgba(0,0,0,0.5);">Eso es gestionar la consecuencia, no el riesgo.</p>
                            <button class="btn-reveal" id="btnRevealIceberg"><i class="fa-solid fa-eye"></i> Mostrar lo Oculto</button>
                        </div>
                    </div>
                </div>
            </section>

            <!-- Slide 04: Contextos -->
            <section>
                <h2>El Contexto de la Hidrovía</h2>
                <p>Las condiciones de aislamiento y las guardias 6/6 potencian los síntomas clínicos <sup><a href="#/10">10-17</a></sup></p>
                <div class="quadrants-grid">
                    <div class="quadrant quadrant-tl">
                        <h3 class="text-red"><i class="fa-solid fa-heart-pulse"></i> Cuadrante Físico</h3>
                        <ul>
                            <li>Fatiga crónica y agotamiento</li>
                            <li>Alteraciones severas del sueño</li>
                            <li>Dolores musculoesqueléticos</li>
                            <li>Hipertensión y somatización</li>
                        </ul>
                    </div>
                    <div class="quadrant quadrant-tr">
                        <h3 class="text-blue"><i class="fa-solid fa-brain"></i> Cuadrante Emocional</h3>
                        <ul>
                            <li>Ansiedad y tensión permanente</li>
                            <li>Episodios depresivos o apatía</li>
                            <li>Irritabilidad e hipersensibilidad</li>
                            <li>Sensación de encierro/atrapamiento</li>
                        </ul>
                    </div>
                    <div class="quadrant quadrant-bl">
                        <h3 class="text-orange"><i class="fa-solid fa-person-running"></i> Cuadrante Conductual</h3>
                        <ul>
                            <li>Negligencia procedural (Piloto automático)</li>
                            <li>Consumo de sustancias (Automedicación)</li>
                            <li>Conductas de riesgo imprudentes</li>
                            <li>Falta de apetito o atracones</li>
                        </ul>
                    </div>
                    <div class="quadrant quadrant-br">
                        <h3 class="text-green"><i class="fa-solid fa-users"></i> Cuadrante Relacional</h3>
                        <ul>
                            <li>Conflictos directos con la tripulación</li>
                            <li>Aislamiento social a bordo</li>
                            <li>Ruptura de vínculos familiares en tierra</li>
                            <li>Insubordinación o fricción con mandos</li>
                        </ul>
                    </div>
                </div>
            </section>

            <!-- Slide 05: Mapeo Clínico -->
            <section>
                <h2>Mapeo Clínico Interactivo (Red Neuronal)</h2>
                <div class="clinical-mapping">
                    
                    <!-- Columna Izquierda: Botones -->
                    <div class="diagnosis-list">
                        <button class="diag-btn active" onclick="loadDiagnosis(0)">1. Trastorno de Ansiedad</button>
                        <button class="diag-btn" onclick="loadDiagnosis(1)">2. Trastorno del Sueño</button>
                        <button class="diag-btn" onclick="loadDiagnosis(2)">3. Síndrome de Burnout</button>
                        <button class="diag-btn" onclick="loadDiagnosis(3)">4. Trastornos de Alimentación</button>
                        <button class="diag-btn" onclick="loadDiagnosis(4)">5. Estrés Postraumático (TEPT)</button>
                        <button class="diag-btn" onclick="loadDiagnosis(5)">6. Depresión</button>
                        <button class="diag-btn" onclick="loadDiagnosis(6)">7. Trastorno Explosivo (Ira)</button>
                    </div>

                    <!-- Columna Central: Síntomas -->
                    <div class="symptoms-display" id="symptomsBox">
                        <h3 id="diagTitle" class="text-blue" style="margin-top:0;">Trastorno de Ansiedad</h3>
                        <div id="diagContent" style="font-size: 1.1rem; line-height: 1.6;">
                            <!-- Contenido dinámico -->
                        </div>
                    </div>

                    <!-- Columna Derecha: Pérdidas -->
                    <div class="losses-list-col" id="lossesNodes">
                        <div class="loss-node" id="node-1">1. Accidentes <span class="loss-badge"></span></div>
                        <div class="loss-node" id="node-2">2. Absentismo <span class="loss-badge"></span></div>
                        <div class="loss-node" id="node-3">3. Alta Rotación <span class="loss-badge"></span></div>
                        <div class="loss-node" id="node-4">4. Errores <span class="loss-badge"></span></div>
                        <div class="loss-node" id="node-5">5. Daño Carga <span class="loss-badge"></span></div>
                        <div class="loss-node" id="node-6">6. Sanciones <span class="loss-badge"></span></div>
                        <div class="loss-node" id="node-7">7. Baja Eficiencia <span class="loss-badge"></span></div>
                        <div class="loss-node" id="node-8">8. Conflictos <span class="loss-badge"></span></div>
                        <div class="loss-node" id="node-9">9. Sin Contratos <span class="loss-badge"></span></div>
                        <div class="loss-node" id="node-10">10. Litigios <span class="loss-badge"></span></div>
                    </div>

                </div>
            </section>

            <!-- Slide 06: Dominó -->
            <section>
                <h2>El Costo de la Inacción <sup><a href="#/10">10-17</a></sup></h2>
                <p>¿Qué pasa si la empresa decide "esperar y ver"?</p>
                
                <div class="domino-track">
                    <div class="domino" id="domino1">Falta de Descanso<br><small>(Click)</small></div>
                    <div class="domino">1.<br>Más Errores</div>
                    <div class="domino">2.<br>Más Accidentes</div>
                    <div class="domino">3.<br>Más Rotación</div>
                    <div class="domino">4.<br>Más Licencias</div>
                    <div class="domino">5.<br>Costos Médicos</div>
                    <div class="domino">6.<br>Baja Producción</div>
                    <div class="domino">7.<br>Sin Compromiso</div>
                    <div class="domino">8.<br>Conflictos</div>
                    <div class="domino" style="background:var(--alert-red);"><i class="fa-solid fa-dollar-sign"></i><br>Impacto Financiero</div>
                </div>

                <div class="domino-desc" id="dominoDescText">
                    Haz clic en la primera ficha (Falta de Descanso) para observar el efecto cascada hacia las pérdidas financieras y operativas.
                </div>
            </section>

            <!-- Slide 07: Pilares -->
            <section>
                <h2>Programa "Gente Saludable"</h2>
                <p>"Transformando el Riesgo Psicosocial en Rentabilidad Operativa"</p>
                <div class="pillars-grid">
                    <div class="pillar-card">
                        <h3><i class="fa-solid fa-user-doctor"></i> 1. Atención Psicológica</h3>
                        <p><strong>Enfoque:</strong> Intervención en Ansiedad, Depresión y desgaste familiar. Recuperación de afrontamiento.</p>
                        <p class="text-green"><strong>ROI:</strong> Reduce absentismo médico, alta rotación y presentismo.</p>
                    </div>
                    <div class="pillar-card">
                        <h3><i class="fa-solid fa-kit-medical"></i> 2. Primeros Auxilios (PAP)</h3>
                        <p><strong>Enfoque:</strong> "Ver, Escuchar y Vincular" ante situaciones críticas/accidentes.</p>
                        <p class="text-green"><strong>ROI:</strong> Reduce TEPT, mitiga errores humanos severos post-incidente.</p>
                    </div>
                    <div class="pillar-card">
                        <h3><i class="fa-solid fa-phone-volume"></i> 3. Guardia Clínica 24/7</h3>
                        <p><strong>Enfoque:</strong> Canal de contención inmediata para crisis.</p>
                        <p class="text-green"><strong>ROI:</strong> Prevención de conductas imprudentes, reduce conflictos sindicales/violencia.</p>
                    </div>
                    <div class="pillar-card">
                        <h3><i class="fa-solid fa-chalkboard-user"></i> 4. Charlas Preventivas</h3>
                        <p><strong>Enfoque:</strong> Herramientas psicoeducativas (gestión de estrés, sueño).</p>
                        <p class="text-green"><strong>ROI:</strong> Disminución de accidentes por fatiga mejorando la higiene del sueño.</p>
                    </div>
                </div>
            </section>

            <!-- Slide 08: Tabla PAP -->
            <section>
                <h2>Utilidad de los Primeros Auxilios Psicológicos (PAP) <sup><a href="#/10">18,19</a></sup></h2>
                
                <table class="styled-table">
                    <thead>
                        <tr>
                            <th>Indicador de Respuesta</th>
                            <th>Capacitación (Sin PAP) <i class="fa-solid fa-xmark" style="color:#ffcccc;"></i></th>
                            <th>Capacitación (Con PAP) <i class="fa-solid fa-check" style="color:#ccffcc;"></i></th>
                        </tr>
                    </thead>
                    <tbody>
                        <tr>
                            <td><strong>Detección y contención inicial</strong></td>
                            <td>La intervención se basa en la improvisación, pudiendo empeorar la angustia.</td>
                            <td>Presencia compasiva y escucha reflexiva para estabilizar reacciones agudas.</td>
                        </tr>
                        <tr>
                            <td><strong>Evaluación de urgencia (Triaje)</strong></td>
                            <td>Riesgo de desperdiciar recursos sin distinguir estrés temporal de disfunción severa.</td>
                            <td>Triaje estructurado para identificar inestabilidad y priorizar atención.</td>
                        </tr>
                        <tr>
                            <td><strong>Mitigación del estrés agudo</strong></td>
                            <td>Empeoramiento psicológico y reacciones impulsivas sin manejo.</td>
                            <td>Tácticas de reencuadre y orientación para fomentar mecanismos de afrontamiento.</td>
                        </tr>
                        <tr>
                            <td><strong>Resolución y seguimiento</strong></td>
                            <td>Incidente concluye sin directriz clara ni orientación de pasos a seguir.</td>
                            <td>Facilita acceso a atención continua, determinando capacidad o necesidad de derivación.</td>
                        </tr>
                    </tbody>
                </table>
                <p style="font-size:0.9rem; text-align:justify;"><strong>Para Empresas:</strong> Actúan como multiplicador de fuerza, mitigan disfunciones operativas inmediatas y reducen trastornos prolongados.</p>
            </section>

            <!-- Slide 09: Ética -->
            <section>
                <h2>El Compromiso Ético y Corporativo</h2>
                
                <div style="text-align: center; margin-top: 40px;">
                    <ul class="ethics-list">
                        <li><span class="ethics-no"><i class="fa-solid fa-xmark"></i> NO</span> es una auditoría punitiva de la tripulación.</li>
                        <li><span class="ethics-no"><i class="fa-solid fa-xmark"></i> NO</span> se realizan evaluaciones de rendimiento operativo.</li>
                        <li><span class="ethics-no"><i class="fa-solid fa-xmark"></i> NO</span> se revelan historiales clínicos individuales a la empresa.</li>
                        <li style="margin-top:20px;"><span class="ethics-yes"><i class="fa-solid fa-check-double"></i> SÍ</span> garantizamos estricto secreto profesional clínico.</li>
                    </ul>
                </div>

                <div class="bonus-box">
                    <h3><i class="fa-solid fa-gift"></i> Beneficio Adicional Exclusivo</h3>
                    <p style="font-size: 1.1rem; margin-bottom: 5px;">La contratación incluye <strong>sin costo adicional</strong> una Charla de Socialización On-Board o en Base.</p>
                    <p style="font-size: 1rem; color: #e0e0e0;"><strong>Objetivo:</strong> Derribar el estigma cultural, explicar la confidencialidad y potenciar el uso preventivo del servicio clínico (fisiológico y psicológico).</p>
                </div>
            </section>

            <!-- Slide 10: Contacto -->
            <section>
                <div class="contact-box">
                    <img src="logofblancovector.jpg" alt="Gente Saludable Logo">
                    <h2>Haga una cita</h2>
                    <p>Agende una reunión para evaluar la implementación<br>de un programa a medida en su flota.</p>
                    
                    <div class="contact-info">
                        <p><i class="fa-brands fa-whatsapp text-green"></i> +595 994 532233</p>
                        <p><i class="fa-regular fa-envelope text-blue"></i> info@gentesaludablepy.com</p>
                    </div>
                </div>
            </section>

            <!-- Slide 11: Referencias -->
            <section id="10">
                <h2>Referencias Bibliográficas</h2>
                <div class="refs-container">
                    <ol>
                        <li>Rozadilla, B. (2018). Paraguay: una economía potenciada desde el agro (parte II). Informativo Semanal BCR.</li>
                        <li>Laurell, A. C. (Coord.). (1993). Para la investigación sobre la salud de los trabajadores. OPS.</li>
                        <li>CEPAL. (2020). Protección social universal en América Latina y el Caribe. Naciones Unidas.</li>
                        <li>Noriega, M. (1993). Organización laboral, exigencias y enfermedad. OPS.</li>
                        <li>Buere, G. (2014). El desarrollo de infraestructuras en América del Sur: Hidrovía. UDELAR.</li>
                        <li>CAFYM. (2017). Informes estadísticos sobre tráfico fluvial.</li>
                        <li>OIT. (2016). Panorama Laboral 2016: América Latina y el Caribe.</li>
                        <li>Novick, M. (1993). Alcances y críticas de los métodos de medición objetivos. OPS.</li>
                        <li>Méndez, R. (2007). Tratado de Medicina del Trabajo (Vol. I). Elsevier.</li>
                        <li>Gil Hernández, F. (2012). Tratado de medicina del trabajo. Elsevier Masson.</li>
                        <li>Leonardi, F. (2024). Imparare a dormire: Guida pratica contro l'insonnia. Ponte alle Grazie.</li>
                        <li>Moreno Jiménez, B. (2011). Factores y riesgos laborales psicosociales. Medicina y Seguridad del Trabajo.</li>
                        <li>Muriana, E., Pettenò, L., & Verbitz, T. (2007). Las caras de la depresión. Herder.</li>
                        <li>Nardone, G. (2007). Miedo, pánico, fobias: La terapia breve. Herder.</li>
                        <li>Nardone, G. (2014). Psicotrampas. Paidós.</li>
                        <li>Ruiz-Frutos, C. et al. (2022). Salud laboral (5ª ed.). Elsevier.</li>
                        <li>van der Kolk, B. (2015). El cuerpo lleva la cuenta. Editorial Eleftheria.</li>
                        <li>Everly, G. S., Jr., & Lating, J. M. (2022). The Johns Hopkins Guide to Psychological First Aid.</li>
                        <li>Manual de PAP Cruz Roja.</li>
                        <li>American Psychiatric Association. (2014). DSM-5. American Psychiatric Publishing.</li>
                    </ol>
                </div>
            </section>

        </div>
    </div>

    <!-- Scripts -->
    <script src="https://cdnjs.cloudflare.com/ajax/libs/reveal.js/4.3.1/reveal.min.js"></script>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/gsap/3.12.2/gsap.min.js"></script>

    <script>
        // Inicializar Reveal.js
        Reveal.initialize({
            width: 1600,
            height: 900,
            margin: 0.1,
            hash: true,
            transition: 'slide', // none/fade/slide/convex/concave/zoom
            controls: true,
            progress: true,
            center: true
        });

        // --------------------------------------------------------
        // SLIDE 1: Animación Hero
        // --------------------------------------------------------
        Reveal.on('slidechanged', event => {
            if (event.indexh === 0) {
                gsap.fromTo('.hero-title', 
                    { y: 50, opacity: 0 }, 
                    { y: 0, opacity: 1, duration: 1.5, ease: "power3.out" }
                );
            }
        });
        // Trigger on load for the first time
        gsap.fromTo('.hero-title', { y: 50, opacity: 0 }, { y: 0, opacity: 1, duration: 1.5, ease: "power3.out", delay: 0.5 });

        // --------------------------------------------------------
        // SLIDE 2: Datos de Pérdidas Ocultas
        // --------------------------------------------------------
        const lossesData = {
            1: { title: "1. Accidentes por Fatiga", desc: "El error humano originado por el déficit de sueño en maniobras críticas es una de las principales causas de colisiones y varaduras. En la Hidrovía Paraguay-Paraná, las demoras causadas por accidentes o bajantes mal gestionadas imponen altos sobrecostos, afectando severamente el flujo de barcazas.", impact: "USD $50,000 - $200,000+" },
            2: { title: "2. Absentismo Médico", desc: "Las licencias psiquiátricas y médicas derivadas de las altas exigencias laborales exigen reemplazos urgentes, lo que implica el traslado rápido de personal a puertos intermedios y el pago de salarios dobles para no detener las operaciones.", impact: "USD $5,000 - $15,000 / mes" },
            3: { title: "3. Alta Rotación", desc: "La precariedad, el aislamiento fluvial y la falta de condiciones óptimas propician la renuncia de oficiales y tripulantes clave. Los procesos de reclutamiento y evaluación médica de nuevos navegantes representan gastos fijos muy elevados.", impact: "USD $10,000 - $25,000 c/u" },
            4: { title: "4. Errores Sub-notificados", desc: "El temor a sanciones y el estrés operativo permanente fomentan que las tripulaciones oculten incidentes menores o negligencias operativas. Estos fallos latentes terminan causando un desgaste acelerado a las maquinarias.", impact: "USD $20,000 - $50,000" },
            5: { title: "5. Daño a la Carga", desc: "El manejo deficiente, las alteraciones en la coordinación del equipo o la falta de concentración durante el estibaje y la navegación derivan en la merma o ruina de la mercancía. En el corredor hidroviario, esto afecta principalmente a la soja.", impact: "USD $15,000 - $80,000" },
            6: { title: "6. Sanciones por Incumplimiento Normativo", desc: "La sobreexigencia en las jornadas y la falta de planificación en los relevos generan infracciones a los códigos laborales de navegación vigentes. Esto resulta en fuertes multas e inmovilización de buques.", impact: "USD $10,000 - $30,000" },
            7: { title: "7. Baja Eficiencia (Presentismo)", desc: "Los tripulantes asisten, pero rinden muy por debajo de los estándares debido al agotamiento mental, el burnout y la apatía. Esto disminuye la eficiencia logística, prolongando tiempos y generando gasto en combustible.", impact: "15% de caída operativa" },
            8: { title: "8. Conflictos Sindicales", desc: "Un clima laboral hostil y autoritario deteriora gravemente las relaciones a bordo y en puertos. Esta situación de tensión se traduce en reclamos colectivos, huelgas y paros.", impact: "Lucro cesante diario" },
            9: { title: "9. Pérdida de Contratos", desc: "El deterioro progresivo de la imagen corporativa frente a los grandes agroexportadores (debido a la falta de fiabilidad en las operaciones y accidentes) bloquea las negociaciones a largo plazo.", impact: "Impacto a largo plazo" },
            10: { title: "10. Litigios Laborales", desc: "El desgaste profesional agudo y las enfermedades de origen laboral vinculadas a la falta de medidas de higiene, seguridad y salud mental abren la puerta a demandas costosas y peritajes médicos judiciales.", impact: "USD $100,000+" }
        };

        function openLossDetail(id) {
            document.getElementById('lossTitle').innerText = lossesData[id].title;
            document.getElementById('lossDesc').innerText = lossesData[id].desc;
            document.getElementById('lossImpact').innerText = lossesData[id].impact;
            
            const overlay = document.getElementById('lossOverlay');
            overlay.classList.add('active');
            gsap.fromTo(overlay, {opacity: 0, scale: 0.9}, {opacity: 1, scale: 1, duration: 0.3});
        }
        function closeLossDetail() {
            const overlay = document.getElementById('lossOverlay');
            gsap.to(overlay, {opacity: 0, scale: 0.9, duration: 0.3, onComplete: () => overlay.classList.remove('active')});
        }

        // --------------------------------------------------------
        // SLIDE 3: Iceberg Animation
        // --------------------------------------------------------
        document.getElementById('btnRevealIceberg').addEventListener('click', () => {
            gsap.to('#icebergCover', { y: '100%', opacity: 0, duration: 1.5, ease: "power2.inOut" });
        });
        // Reset iceberg on slide change
        Reveal.on('slidechanged', event => {
            if (event.indexh !== 2) {
                gsap.set('#icebergCover', { y: '0%', opacity: 1 });
            }
        });

        // --------------------------------------------------------
        // SLIDE 5: Mapeo Clínico Interactivo
        // --------------------------------------------------------
        const clinicalDB = [
            {
                title: "1. Trastorno de Ansiedad",
                symptoms: `
                    <p><b><i class="fa-solid fa-heart-pulse text-red"></i> Físico:</b> Taquicardia, opresión torácica, tensión muscular y sudoración.</p>
                    <p><b><i class="fa-solid fa-brain text-blue"></i> Emocional:</b> Rumiación catastrófica, tensión permanente y miedo a perder el control.</p>
                    <p><b><i class="fa-solid fa-person-running text-orange"></i> Conductual:</b> Hiperactividad nerviosa, intentos disfuncionales de control y evitación de maniobras complejas.</p>
                    <p><b><i class="fa-solid fa-users text-green"></i> Relacional:</b> Dependencia excesiva de compañeros para reaseguro o irritabilidad por hipervigilancia.</p>
                `,
                losses: [ {id: 2, val: "40%"}, {id: 4, val: "30%"}, {id: 7, val: "30%"} ]
            },
            {
                title: "2. Trastorno del Sueño",
                symptoms: `
                    <p><b>Físico:</b> Fatiga crónica, agotamiento profundo y alteraciones severas del sueño.</p>
                    <p><b>Emocional:</b> Irritabilidad, hipersensibilidad al estrés y frustración.</p>
                    <p><b>Conductual:</b> Negligencia procedural (piloto automático), microsueños, pérdida de atención.</p>
                    <p><b>Relacional:</b> Aislamiento social a bordo por falta de energía para socializar.</p>
                `,
                losses: [ {id: 1, val: "50%"}, {id: 5, val: "30%"}, {id: 7, val: "20%"} ]
            },
            {
                title: "3. Síndrome de Burnout",
                symptoms: `
                    <p><b>Físico:</b> Agotamiento extremo y dolores musculoesqueléticos.</p>
                    <p><b>Emocional:</b> Cinismo, despersonalización y sensación de encierro.</p>
                    <p><b>Conductual:</b> Presentismo pasivo, inercia, negligencia procedural.</p>
                    <p><b>Relacional:</b> Insubordinación silenciosa, fricción con mandos.</p>
                `,
                losses: [ {id: 3, val: "40%"}, {id: 7, val: "40%"}, {id: 10, val: "20%"} ]
            },
            {
                title: "4. Trastornos de Alimentación",
                symptoms: `
                    <p><b>Físico:</b> Alteraciones metabólicas, fluctuaciones de peso, trastornos gastrointestinales.</p>
                    <p><b>Emocional:</b> Consumo o restricción como intento de control de emociones.</p>
                    <p><b>Conductual:</b> Atracones compulsivos o falta de apetito extrema.</p>
                    <p><b>Relacional:</b> Aislamiento social a bordo (esconder comida o evitar comedor).</p>
                `,
                losses: [ {id: 2, val: "50%"}, {id: 7, val: "30%"}, {id: 4, val: "20%"} ]
            },
            {
                title: "5. Estrés Postraumático",
                symptoms: `
                    <p><b>Físico:</b> Hiperactivación autonómica ("lucha o huida") ante recordatorios.</p>
                    <p><b>Emocional:</b> Terror, tensión permanente, embotamiento emocional y disociación.</p>
                    <p><b>Conductual:</b> Evitación extrema, reacciones de sobresalto exageradas, automedicación.</p>
                    <p><b>Relacional:</b> Desapego, incapacidad para mantener vínculos de confianza.</p>
                `,
                losses: [ {id: 2, val: "50%"}, {id: 10, val: "30%"}, {id: 3, val: "20%"} ]
            },
            {
                title: "6. Depresión",
                symptoms: `
                    <p><b>Físico:</b> Fatiga extrema (astenia), dolores sin causa médica, alteraciones peso/sueño.</p>
                    <p><b>Emocional:</b> Sentimientos de inutilidad, apatía profunda, dolor moral, desesperanza.</p>
                    <p><b>Conductual:</b> Inhibición conductual, lentitud psicomotora, abandono de tareas.</p>
                    <p><b>Relacional:</b> Aislamiento social severo, retracción de comunicación, alejamiento familiar.</p>
                `,
                losses: [ {id: 7, val: "50%"}, {id: 2, val: "30%"}, {id: 4, val: "20%"} ]
            },
            {
                title: "7. Trastorno Explosivo (Ira)",
                symptoms: `
                    <p><b>Físico:</b> Tensión física extrema, descargas de adrenalina mal gestionadas, hipertensión.</p>
                    <p><b>Emocional:</b> Irritabilidad crónica, intolerancia a frustración, hostilidad.</p>
                    <p><b>Conductual:</b> Arrebatos de furia, conductas de riesgo imprudentes, agresión.</p>
                    <p><b>Relacional:</b> Conflictos violentos, destrucción clima laboral, insubordinación grave.</p>
                `,
                losses: [ {id: 8, val: "40%"}, {id: 9, val: "30%"}, {id: 6, val: "30%"} ]
            }
        ];

        function loadDiagnosis(index) {
            // Activar boton
            document.querySelectorAll('.diag-btn').forEach((btn, i) => {
                btn.classList.toggle('active', i === index);
            });

            const data = clinicalDB[index];
            
            // Animar entrada de síntomas
            const contentBox = document.getElementById('symptomsBox');
            gsap.to(contentBox, { opacity: 0, duration: 0.2, onComplete: () => {
                document.getElementById('diagTitle').innerText = data.title;
                document.getElementById('diagContent').innerHTML = data.symptoms;
                gsap.to(contentBox, { opacity: 1, y: 0, duration: 0.4, ease: "power2.out" });
            }});

            // Limpiar nodos
            document.querySelectorAll('.loss-node').forEach(node => {
                node.classList.remove('highlighted');
                node.querySelector('.loss-badge').innerText = '';
            });

            // Animar nodos correspondientes
            data.losses.forEach(loss => {
                const node = document.getElementById('node-' + loss.id);
                if(node) {
                    node.classList.add('highlighted');
                    node.querySelector('.loss-badge').innerText = loss.val;
                }
            });
        }
        // Init first one
        loadDiagnosis(0);

        // --------------------------------------------------------
        // SLIDE 6: Animación Dominó
        // --------------------------------------------------------
        document.getElementById('domino1').addEventListener('click', () => {
            gsap.to('.domino', {
                rotation: 65, 
                x: 30,
                transformOrigin: "bottom right", 
                stagger: 0.15, 
                ease: "bounce.out",
                duration: 1
            });
            
            gsap.to('#dominoDescText', {
                opacity: 0,
                duration: 0.5,
                onComplete: () => {
                    document.getElementById('dominoDescText').innerHTML = `
                        <p class="text-red" style="font-weight:bold; font-size:1.3rem;">El Colapso es Inevitable si solo reaccionamos al final.</p>
                        <p>La inacción ante la fatiga inicial genera una reacción en cadena. El estrés no atendido se convierte en negligencia procedural (piloto automático), que a su vez causa siniestros y desgasta al equipo. Esto eleva los costos médicos, las licencias y la rotación, destruyendo el clima laboral y desembocando en conflictos y un <strong>impacto financiero irreversible</strong> para la naviera.</p>
                    `;
                    gsap.to('#dominoDescText', { opacity: 1, duration: 0.5 });
                }
            })
        });

        Reveal.on('slidechanged', event => {
            if (event.indexh !== 5) {
                // Reset domino
                gsap.set('.domino', { rotation: 0, x: 0 });
                document.getElementById('dominoDescText').innerHTML = "Haz clic en la primera ficha (Falta de Descanso) para observar el efecto cascada hacia las pérdidas financieras y operativas.";
            }
        });

    </script>
</body>
</html>
"""

with open("index.html", "w", encoding="utf-8") as f:
    f.write(html_content)

print("index.html has been generated successfully.")