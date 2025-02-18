#include "stdafx.h"
#include <iostream> // wcin, wcout
#include <speechapi_cxx.h>

using namespace std;
using namespace Microsoft::CognitiveServices::Speech;

void recognizeSpeech() {
	wstring subscriptionKey{ L"a9b86d09dbc046ffa92b72d7d1b2557f" };
	wstring region{ L"westus" };

	auto factory = SpeechFactory::FromSubscription(subscriptionKey, region);
	auto recognizer = factory->CreateSpeechRecognizer();
	//auto recognizer = factory->CreateSpeechRecognizerWithFileInput(L"11sec.wav");

	wcout << "Say something...\n";
	auto future = recognizer->RecognizeAsync();
	auto result = future.get();

	if (result->Reason != Reason::Recognized) {
		wcout << L"There was an error, reason " << int(result->Reason) << L" - " << result->ErrorDetails << '\n';
	}
	else {
		wcout << L"We recognized: " << result->Text << '\n';
	}
	wcout << L"Please press a key to continue.\n";
	wcin.get();
}

int main()
{
	recognizeSpeech();
	return 0;
}