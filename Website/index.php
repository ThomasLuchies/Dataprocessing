<!DOCTYPE html>
<html>
    <head>
        <title>asteroid</title>
        <link href="style.css" rel="stylesheet" type="text/css">    
    </head>
    <body>
        <div id="container">
            <div id="left">
                <p><strong>Get classification for asteroid</strong></p>
                <form method="post" id="classificationForm" action="<?php echo htmlspecialchars($_SERVER["PHP_SELF"]);?>">
                    <input type="text" placeholder="absolute magnitude" name="absoluteMagnitude">
                    <input type="text" placeholder="est dia in km" name="estDiaInKm">
                    <input type="text" placeholder="est dia in m" name="estDiaInM">
                    <input type="text" placeholder="est dia in miles" name="estDiaInMiles">
                    <input type="text" placeholder="est dia in feet" name="estDiaInFeet">
                    <input type="submit" name="submit" value="submt">
                </form>
                <?php
                    $currentClassication = null;
                    if(isset($_POST["submit"]))
                    {
                        $absoluteMagnitude = $_POST["absoluteMagnitude"];
                        $estDiaInKm = $_POST["estDiaInKm"];
                        $estDiaInM = $_POST["estDiaInM"];
                        $estDiaInMiles = $_POST["estDiaInMiles"];
                        $estDiaInFeet = $_POST["estDiaInFeet"];
                        $response = file_get_contents("http://localhost:8000/classifications/");
                        $classificationArray = json_decode($response, true);
                        foreach($classificationArray as $classification)
                        {
                            if($absoluteMagnitude == $classification["absoluteMagnitude"])
                            {
                                if($estDiaInKm > $classification["estDiaInKmMin"] && $estDiaInKm < $classification["estDiaInKmMax"])
                                {
                                    if($estDiaInM > $classification["estDiaInMMin"] && $estDiaInM < $classification["estDiaInMMax"])
                                    {
                                        if($estDiaInMiles > $classification["estDiaInMilesMin"] && $estDiaInMiles < $classification["estDiaInMilesMax"])
                                        {
                                            if($estDiaInFeet > $classification["estDiaInFeetMin"] && $estDiaInFeet < $classification["estDiaInFeetMax"])
                                            {
                                                $currentClassication = $classification["name"];
                                            }
                                        }
                                    }
                                }
                            }
                        }
                    }
                    if($currentClassication != null)
                    {
                        echo "The classicitation of the asteroid is " . $currentClassication;
                    }
                    else 
                    {
                        echo "There was no classification found";
                    }
                ?>  
            </div>
            <div id="center">
                <p><strong>Orbits</strong></p>
                <?php
                    $request = file_get_contents("http://localhost:8000/orbits/");
                    $requestArray = json_decode($request, true);
                    foreach($requestArray as $request)
                    {
                        echo "<div class='cell'>" . "<br>";
                        echo "Name:" . $request["name"] . "<br>";
                        echo "Epoch:" . $request["epoch"] . "<br>";
                        echo "Orbit Axis:" . $request["orbitAxis"] . "<br>";
                        echo "Orbit Eccentricity: " . $request["orbitEccentricity"] . "<br>";
                        echo "Orbit Inclanation: " . $request["orbitInclanation"] . "<br>";
                        echo "Perihelion Argument :" . $request["periphelionArgument"] . "<br>";
                        echo "Node Longitude: " . $request["nodeLongitude"] . "<br>";
                        echo "Mean Anomaly: " . $request["meanAnomaly"] . "<br>";
                        echo "Absolute Magnitude: " . $request["absoluteMagnitude"] . "<br>";
                        echo "Periphelion Distance: " . $request["periphelionDistance"] . "<br>";
                        echo "</div>"; 
                    }
                ?>
            </div>

            <div id="right">
                <p><strong>Impacts</strong></p>
                <?php
                    $request = file_get_contents("http://localhost:8000/impacts/");
                    $requestArray = json_decode($request, true);
                    foreach($requestArray as $request)
                    {
                        echo "<div class='cell'>" . "<br>";
                        echo "fullName:" . $request["fullName"] . "<br>";
                        echo "periodStart:" . $request["periodStart"] . "<br>";
                        echo "periodEnd:" . $request["periodEnd"] . "<br>";
                        echo "possibleImpacts: " . $request["possibleImpacts"] . "<br>";
                        echo "cumulativeImpactProbability: " . $request["cumulativeImpactProbability"] . "<br>";
                        echo "asteroidVelocity :" . $request["asteroidVelocity"] . "<br>";
                        echo "cumulativePalermoScale: " . $request["cumulativePalermoScale"] . "<br>";
                        echo "maximumPalermoScale: " . $request["maximumPalermoScale"] . "<br>";
                        echo "Absolute Magnitude: " . $request["absoluteMagnitude"] . "<br>";
                        echo "</div>"; 
                    }
                ?>
            </div>
        </div>
    </body>
</html>