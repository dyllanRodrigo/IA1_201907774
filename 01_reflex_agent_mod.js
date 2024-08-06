function reflex_agent(location, state) {
	if (state == "DIRTY") return "SUCK";
	else if (location == "A") return "RIGHT";
	else if (location == "B") return "LEFT";
  }

  function allStatesVisited(states, visited) {
	for (let i = 0; i < visited.length; i++) {
	  if (visited[i][0] === states[0] && visited[i][1] === states[1] && visited[i][2] === states[2]) {
		return true;
	  }
	}
	return false;
  }

  function test(states, visited) {
	if (visited.length >= 8) {
	  document.getElementById("log").innerHTML += "<br>All states visited!";
	  return;
	}

	var location = states[0];
	var state = location == "A" ? states[1] : states[2];
	var action_result = reflex_agent(location, state);
	document.getElementById("log").innerHTML += "<br>Location: " + location + " | Action: " + action_result;

	if (action_result == "SUCK") {
	  if (location == "A") states[1] = "CLEAN";
	  else if (location == "B") states[2] = "CLEAN";
	} else if (action_result == "RIGHT") states[0] = "B";
	else if (action_result == "LEFT") states[0] = "A";

	if (!allStatesVisited(states, visited)) {
	  visited.push([states[0], states[1], states[2]]);
	}

	setTimeout(function() { test(states, visited); }, 2000);
  }

  var states = ["A", "DIRTY", "DIRTY"];
  var visited = [];
  test(states, visited);