document
  .getElementById("compare-ip-form")
  .addEventListener("submit", function (event) {
    event.preventDefault(); // Prevent form submission

    const ip1 = document.getElementById("ip1").value;
    const ip2 = document.getElementById("ip2").value;

    fetchIpInfo(ip1, "ip1");
    fetchIpInfo(ip2, "ip2");
  });

function fetchIpInfo(ip, ipLabel) {
  fetch(`https://ipapi.co/${ip}/json/`)
    .then((response) => {
      if (!response.ok) throw new Error("IP not found");
      return response.json();
    })
    .then((data) => displayIpInfo(data, ipLabel))
    .catch((error) => alert(error.message));
}

function displayIpInfo(data, ipLabel) {
  const resultsDiv = document.getElementById("comparison-results");
  const listGroup = document.createElement("div");
  listGroup.className = "col-md-6 list-group";

  const ipInfoHtml = `
    <div class="list-group-item">
        <strong>Public IPv4 Address:</strong> ${data.ip}
    </div>
    <div class="list-group-item">
        <strong>IP Version:</strong> ${data.version}
    </div>
    <div class="list-group-item">
        <strong>ISP:</strong> ${data.org}
    </div>
    <div class="list-group-item">
        <strong>Network:</strong> ${data.network}
    </div>
    <div class="list-group-item">
        <strong>City:</strong> ${data.city}
    </div>
    <div class="list-group-item">
        <strong>Region:</strong> ${data.region}
    </div>
    <div class="list-group-item">
        <strong>Country:</strong> ${data.country_name}
    </div>
`;

  listGroup.innerHTML = ipInfoHtml;
  resultsDiv.appendChild(listGroup);
}
