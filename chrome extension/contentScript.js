//the point of this is to check if the element exists
function waitForElement(querySelector, timeout){
    return new Promise((resolve, reject) => {
        var timer=false;
        let target=document.querySelector('[data-testid="expandable-text-box"]');
        if (target) return resolve();
        const observer=new MutationObserver(()=>{
            if (document.querySelector('[data-testid="expandable-text-box"]')){
                observer.disconnect();
                if (timer!==false) clearTimeout(timer);
                return resolve();
            }
        } );
        observer.observe(document.body, {
            childList: true,
            subtree: true
        });
        if (timeout) timer=setTimeout( ()=> {
            observer.disconnect();
            reject();
        }, timeout);
    }
)}

//this block is for taking the data and sending it to flask 
//after making it into json etc
async function getData(text) {
    const url="http://127.0.0.1:5000/analyze";
    try {
        const response = await fetch(url, {
            method: "POST",
            body: JSON.stringify({text: text}),
            headers: {
                "Content-Type": "application/json"
            }
        });
        if (!response.ok) {
            throw new Error(`Response Status: ${response.status}`);
        }
        const result = await response.json();
        console.log(result);
    } catch(error) {
        console.error(error.message);
    }
}

//making both of them work together
async function main(){
    try{
        await waitForElement('[data-testid="expandable-text-box"]', 5000);
        let text=document.querySelector('[data-testid="expandable-text-box"]').innerText;
        await getData(text);
    }
    catch(error){
        console.error("Element not found within the specified timeout.");
    }
}

main();