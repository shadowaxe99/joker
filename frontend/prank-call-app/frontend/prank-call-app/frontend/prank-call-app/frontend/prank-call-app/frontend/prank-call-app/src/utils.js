export const sendPrankMessage = (name, prankMessage) => {
  return new Promise((resolve, reject) => {
    // Simulating sending prank message
    setTimeout(() => {
      resolve(`Prank message sent by ${name}: ${prankMessage}`);
    }, 2000);
  });
};
