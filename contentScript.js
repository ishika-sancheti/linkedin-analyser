async function downloadBlobAsFile(blob){
    const text=await blob.text()
    chrome.runtime.sendMessage({csvText: text})
    // const fileURL=URL.createObjectURL(blob);
    // chrome.runtime.sendMessage({url: fileURL, fileName: "export.csv"})
}

async function fetchA(keyword) {
    const url="http://127.0.0.1:5000/analyze";
    try {
        const response = await fetch(url, {
            method: "POST",
            body: JSON.stringify({keyword: keyword}),
            headers: {
                "Content-Type": "application/json"
            }
        });
        if (!response.ok) {
            throw new Error(`Response Status: ${response.status}`);
        }
        const result = await response.blob();
        downloadBlobAsFile(result);
    } catch(error) {
        console.error(error.message);
    }
}

async function main(keyword){
    await fetchA(keyword)
}

const keyword=new URL(window.location.href).searchParams.get('keywords')
if (keyword){
    main(keyword)
}
