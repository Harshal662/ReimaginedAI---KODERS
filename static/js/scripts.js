document.addEventListener("DOMContentLoaded", function () {
    var respData;
    // Handle form submission
    document.getElementById('card-hide').classList.add('hidden');
    document.getElementById('card-hide1').classList.add('hidden');
    document.getElementById('card-hide2').classList.add('hidden');

    document.getElementById('high').classList.add('hidden');
    document.getElementById('medium').classList.add('hidden');
    document.getElementById('low').classList.add('hidden');

    const form = document.getElementById("form");
    form.addEventListener("submit", handleFormSubmit);

    // Generate Report button event listener
    const generateReportButton = document.getElementById("generateReport");
    if (generateReportButton) {
        generateReportButton.addEventListener("click", generateReport);
    }

    // Handle form submission
    async function handleFormSubmit(event) {
        event.preventDefault();
        // Collect form data
        const formData = new FormData(form);

        // Simple validation
        if (!formData.get("title") || !formData.get("desc") || !formData.get("summary") ||
            !formData.get("reqType") || !formData.get("priority") || !formData.get("roles") ||
            !formData.get("departments")) {
            alert("Please fill in all fields.");
            return; // Stop submission if any field is missing
        }



        const formObject = {};

        // Convert FormData entries to a plain object
        formData.forEach((value, key) => {
            formObject[key] = value;
        });

        // Convert the object to JSON
        const jsonData = JSON.stringify(formObject);
        // Make the GET request
        fetchData(jsonData)


    }
    // Generate report function
    function fetchData(jsonData) {
        const url = "http://localhost:5000/analyze"
        fetch(url, {
            method: 'POST', // or 'GET' or any other HTTP method
            headers: {
                'Content-Type': 'application/json'  // Define the content type
            },
            body: jsonData
        })
            .then(response => {
                if (!response.ok) {
                    throw new Error('Network response was not ok');
                }
                return response.json();  // Parse the JSON response
            })
            .then(data => {
                respData = data;
                let innerJsonString = respData.result;

                // Optional: Remove line breaks (not strictly needed)
                innerJsonString = innerJsonString.replace(/\n/g, '');

                // Step 2: Parse it into an object
                let parsedData = JSON.parse(innerJsonString);

                if (parsedData) {
                    document.getElementById('imactScore').innerHTML = parsedData?.ImpactScore;
                    const listElementImpStake = document.getElementById('impactedStakeholder')
                    if (parsedData?.ImpactedStakeholderRoles.length) {
                        parsedData.ImpactedStakeholderRoles.forEach(item => {
                            const li = document.createElement("li");
                            li.textContent = item;
                            listElementImpStake.appendChild(li);
                        });
                    }
                    const listElementDept = document.getElementById('ImpactedDept')
                    if (parsedData?.ImpactedDepartments.length) {
                        parsedData.ImpactedDepartments.forEach(item => {
                            const li = document.createElement("li");
                            li.textContent = item;
                            listElementDept.appendChild(li);
                        });
                    }

                    const listElementAffectProc = document.getElementById('AffectedProcesses')
                    if (parsedData?.AffectedProcesses.length) {
                        parsedData.AffectedProcesses.forEach(item => {
                            const li = document.createElement("li");
                            li.textContent = item.name + " - " + item.status;
                            listElementAffectProc.appendChild(li);
                        });
                    }

                  
                    document.getElementById('ReasonForImpact').innerHTML = parsedData?.ReasonForImpact;
                    document.getElementById('ShortSummary').innerHTML = parsedData?.ShortSummary;
                    document.getElementById('relatedRequirements').innerHTML = parsedData?.RelatedRequirements;
                    document.getElementById('inputDataRelevancePercentage').innerHTML = parsedData?.InputDataRelevancePercentage;
                    document.getElementById('card-hide').classList.remove('hidden');
                    document.getElementById('card-hide1').classList.remove('hidden');
                    document.getElementById('card-hide2').classList.remove('hidden');

                    if (parsedData?.RiskLevel.toLocaleLowerCase() === "high") {
                        document.getElementById('high').classList.remove('hidden');
                    } else if (parsedData?.RiskLevel.toLocaleLowerCase() === "medium") {
                        document.getElementById('medium').classList.remove('hidden');
                    } else if (parsedData?.RiskLevel.toLocaleLowerCase() === "low") {
                        document.getElementById('low').classList.remove('hidden');
                    }
                }
            })
            .catch(error => {
                console.error('There was a problem with the fetch operation:', error);
            });
    }

    const jsonString = ``;

    const data = JSON.parse(jsonString);
    const timeToImplement = data.TimeToImplement;

    // Convert time (e.g., "2 weeks" -> 2)
    const categories = Object.keys(timeToImplement);
    const durations = categories.map(category => parseInt(timeToImplement[category]));

    Highcharts.chart('container', {
        chart: {
            type: 'bar'
        },
        title: {
            text: 'Project Time to Implement'
        },
        xAxis: {
            categories: categories,
            title: {
                text: 'Project Phase'
            }
        },
        yAxis: {
            title: {
                text: 'Time (weeks)'
            }
        },
        series: [{
            name: 'Implementation Time',
            data: durations
        }]
    });

    Highcharts.chart('container1', {
        chart: {
            polar: true,
            type: 'line'
        },
        title: {
            text: 'Risk Assumption Analysis',
            x: -80
        },
        pane: {
            size: '80%'
        },
        xAxis: {
            categories: ['Risk', 'Impact', 'Processes', 'Stakeholders', 'Departments'],
            tickmarkPlacement: 'on',
            lineWidth: 0
        },
        yAxis: {
            gridLineInterpolation: 'polygon',
            lineWidth: 0,
            min: 0,
            max: 10,
            title: {
                text: 'Risk Level',
                style: {
                    color: '#aaa'
                }
            }
        },
        series: [{
            name: 'Risk Assumption',
            data: [8, 6, 7, 5, 9], // Example data
            pointPlacement: 'on',
            color: '#FF6347' // Tomato color
        }]
    });
});
function download() {
    alert("Pdf will be downloaded in your browser.")
}
function sendEmail() {
    alert("An Email will be sent to stakeholder DL.")
}