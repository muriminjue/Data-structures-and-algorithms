function recursive_binary_search(list, target) {
  console.log(list);
  if (list.length < 1) {
    return false;
  } else {
    const midpoint = Math.floor(list.length / 2);
    if (list[midpoint] === target) {
      return true;
    } else {
      if (list[midpoint] < target) {
        recursive_binary_search(list.splice(midpoint + 1, list.length), target);
      } else {
        recursive_binary_search(list.splice(0, midpoint), target);
      }
    }
  }
  return false;
}

function verify(result) {
  console.log("Item found: ", result);
}

verify(recursive_binary_search([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 12));
verify(recursive_binary_search([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 6));
