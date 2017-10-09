package sportmanager

import "time"

// Exercise defines an Exercise inside a workout
type Exercise struct {
	Name    string        `json:"name"`
	Sets    int           `json:"sets"`
	Reps    int           `json:"reps"`
	Rest    time.Duration `json:"rest"`
	Note    string        `json:"note"`
	Comment string        `json:"comment"`
}
